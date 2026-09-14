# Outbound Planning | Business Intelligence

Reusable analysis and documented business logic for routing, network performance, RFP evaluation, and transportation cost (TC).

## Purpose
Connect package demand, carrier eligibility, service performance, and transportation economics to a reviewable business decision. Keep the population, assumptions, source versions, and validation evidence with each analysis.

**Template status:** SQL examples use synthetic data. This repository does not contain the production WMS allocator, carrier rate engine, ETL jobs, or live credentials. Migrate approved scripts into the corresponding domain before using production outputs.

## Start here
1. Follow [INSTALL.md](INSTALL.md) to add this template to an existing repository.
2. Review [business rules](docs/business-rules.md) and [source findings](docs/source-findings.md).
3. Copy [the analysis brief](templates/analysis-brief.md) into a dated project folder.
4. Add approved SQL, record source snapshots, and validate the output grain.
5. Open a pull request using the included review checklist.

## Repository map
| Folder | Purpose |
| --- | --- |
| `sql/routing/` | Eligibility, CPT/TNT decisions, modeled allocation, and reconciliation |
| `sql/network_performance/` | DEA, padding, no-POD, induction, and CET/CPT analysis |
| `sql/rfp/` | Candidate demand, exclusions, conversion, and lane economics |
| `sql/transportation_cost/` | Paired package comparisons and gross/net savings |
| `sql/shared/` | Common calendar logic and reusable SQL header |
| `sql/quality/` | Grain, joins, and coverage checks |
| `python/` | Dependency-free, runnable lane-economics example |
| `config/` | Explicit scenario assumptions; historical values are not universal defaults |
| `data/contracts/` | Required input/output definitions |
| `data/samples/` | Synthetic example inputs only |
| `projects/` | Dated analysis briefs and decision records |
| `docs/` | Business definitions, sources, operations, and dashboard catalog |
| `templates/` | Analysis, runbook, decision, and documentation templates |
| `tableau/` | Workbook documentation and deployment notes |
| `tests/` | Economic boundary and error-handling checks |
| `.github/` | PR/issue templates and offline Python validation |

## Run the local example
Requires Python 3.12; the example uses only the standard library.

```bash
python3 python/lane_economics.py --input data/samples/lane_inputs.csv --config config/rfp_fy26_example.json --output outputs/lane_economics.csv
python3 -m unittest discover -s tests -v
```

The example applies the selected rounding policy to converted weekly demand, then subtracts middle-mile cost from gross package entitlement. Input CPPs must already describe the same retained package population and approved scenario. It does not calculate carrier rates or allocate WMS volume.

## Working conventions
- Organize reusable production logic by business domain; keep one-off work in `projects/YYYY-MM-DD_topic/`.
- Record package grain, date basis, effective dates, source freshness, cost scope, and exclusions before interpreting an output.
- Use weighted CPP: total cost / matched rated package count. Report unmatched coverage separately.
- Treat eligibility, modeled allocation, actual allocation, and carrier ratings as separate concepts.
- Keep production connection details and raw package extracts outside Git. Repository access should match the sensitivity of internal logic.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the development workflow and [validation](docs/validation.md) for required analytical evidence.
