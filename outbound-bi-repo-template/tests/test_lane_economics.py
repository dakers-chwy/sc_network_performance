import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
from lane_economics import calculate


class LaneEconomicsTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(scenario_id="TEST", fc="DEMO", lane="A", retained_packages=800,
                        baseline_cpp=3, scenario_cpp=1, cpl_no_fsc=100, min_miles=0)
        self.config = dict(observation_weeks=1, mm_conversion=1, packages_per_load=100,
                           minimum_weekly_loads=7, fuel_per_mile=0, minimum_spl=100,
                           load_rounding="CEIL")

    def test_threshold_is_strict(self):
        result = calculate(self.row, self.config)
        self.assertEqual(result["net_weekly_savings"], Decimal(800))
        self.assertEqual(result["savings_per_load"], Decimal(100))
        self.assertFalse(result["passes_economic_threshold"])

    def test_rounding_policy_changes_loads(self):
        self.row["retained_packages"] = 810
        self.assertEqual(calculate(self.row, self.config)["weekly_loads"], 9)
        self.config["load_rounding"] = "ROUND"
        self.assertEqual(calculate(self.row, self.config)["weekly_loads"], 8)
        self.row["retained_packages"] = 850
        self.assertEqual(calculate(self.row, self.config)["weekly_loads"], 9)

    def test_zero_volume_has_no_loads(self):
        self.row["retained_packages"] = 0
        result = calculate(self.row, self.config)
        self.assertEqual(result["weekly_loads"], 0)
        self.assertIsNone(result["savings_per_load"])
        self.assertFalse(result["passes_economic_threshold"])

    def test_conversion_and_fuel(self):
        self.config.update(mm_conversion="0.5", fuel_per_mile="0.6")
        self.row["min_miles"] = 100
        result = calculate(self.row, self.config)
        self.assertEqual(result["converted_weekly_packages"], 400)
        self.assertEqual(result["weekly_loads"], 7)
        self.assertEqual(result["weekly_mm_cost"], 1120)
        self.assertEqual(result["net_weekly_savings"], -320)

    def test_invalid_inputs_rejected(self):
        for value in (None, "NaN", "Infinity", -1, ""):
            with self.subTest(value=value), self.assertRaises(ValueError):
                calculate({**self.row, "baseline_cpp": value}, self.config)
        with self.assertRaises(ValueError):
            calculate(self.row, {**self.config, "observation_weeks": 0})
        with self.assertRaises(ValueError):
            calculate(self.row, {**self.config, "load_rounding": "UNKNOWN"})


if __name__ == "__main__":
    unittest.main()
