"""Synthetic RFP lane economics. No warehouse access or carrier rating logic."""
import argparse
import csv
import json
from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_HALF_UP
from pathlib import Path


def number(value, name):
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{name} must be numeric") from exc
    if not result.is_finite() or result < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return result


def calculate(row, config):
    values = {key: number(row[key], key) for key in (
        "retained_packages", "baseline_cpp", "scenario_cpp", "cpl_no_fsc", "min_miles"
    )}
    params = {key: number(config[key], key) for key in (
        "observation_weeks", "mm_conversion", "packages_per_load",
        "minimum_weekly_loads", "fuel_per_mile", "minimum_spl"
    )}
    for key in ("observation_weeks", "packages_per_load"):
        if params[key] == 0:
            raise ValueError(f"{key} must be positive")
    if not 0 < params["mm_conversion"] <= 1:
        raise ValueError("mm_conversion must be in (0, 1]")
    for value, name in ((values["retained_packages"], "retained_packages"),
                        (params["minimum_weekly_loads"], "minimum_weekly_loads")):
        if value != value.to_integral_value():
            raise ValueError(f"{name} must be an integer")
    if params["minimum_weekly_loads"] < 1:
        raise ValueError("minimum_weekly_loads must be at least one")
    policy = config["load_rounding"]
    if policy not in ("CEIL", "ROUND"):
        raise ValueError("load_rounding must be CEIL or ROUND")
    identity = {key: str(row[key]).strip() for key in ("scenario_id", "fc", "lane")}
    if not all(identity.values()):
        raise ValueError("scenario_id, fc, and lane must be populated")
    weekly = values["retained_packages"] / params["observation_weeks"]
    converted = weekly * params["mm_conversion"]
    loads = 0
    if converted:
        raw_loads = max(converted / params["packages_per_load"], params["minimum_weekly_loads"])
        loads = int(raw_loads.to_integral_value(
            rounding=ROUND_CEILING if policy == "CEIL" else ROUND_HALF_UP
        ))
    entitlement = converted * (values["baseline_cpp"] - values["scenario_cpp"])
    cost_per_load = values["cpl_no_fsc"] + params["fuel_per_mile"] * values["min_miles"]
    mm_cost = cost_per_load * loads
    savings = entitlement - mm_cost
    spl = savings / loads if loads else None
    return {
        **identity,
        "weekly_packages": weekly,
        "converted_weekly_packages": converted,
        "weekly_loads": loads,
        "gross_weekly_entitlement": entitlement,
        "weekly_mm_cost": mm_cost,
        "net_weekly_savings": savings,
        "savings_per_load": spl,
        "passes_economic_threshold": spl is not None and spl > params["minimum_spl"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.resolve() in (args.input.resolve(), args.config.resolve()):
        parser.error("output must differ from input and config")
    config = json.loads(args.config.read_text(), parse_float=Decimal)
    results, seen = [], set()
    with args.input.open(newline="") as stream:
        for row in csv.DictReader(stream):
            result = calculate(row, config)
            key = tuple(result[name] for name in ("scenario_id", "fc", "lane"))
            if key in seen:
                raise ValueError(f"Duplicate scenario/FC/lane: {key}")
            seen.add(key)
            results.append(result)
    if not results:
        raise ValueError("Input contains no lanes")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    print(f"Wrote {len(results)} synthetic lane results to {args.output}")


if __name__ == "__main__":
    main()
