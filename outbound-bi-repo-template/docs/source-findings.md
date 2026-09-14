# Supplied reference findings

## Sources reviewed
- `OP-FY26 RFP Candidate Determination Logic & Final Output-150526-131848.pdf`: methodology, candidate economics, walkthroughs, and output SQL.
- `comparisons.xlsx`: `BILL_WEIGHT_COMP` (57 data rows, 7 columns) and `ZONE_WEIGHT_BAND_COMP` (52 data rows, 13 columns).

The binary references are not bundled. This template records their relevant definitions; it does not redistribute their detailed rates or claim to reproduce the full model.

## RFP methodology
The PDF evaluates FC→customer ZIP demand serviceable by each candidate station. It removes dedicated volume for FedEx and both dedicated and selected FedEx candidate volume for OnTrac. CPP uses retained volume. Historical example inputs are 83.5% MM conversion, 1,175 packages/load, 7 minimum weekly loads, $0.60 fuel/mile, and a strict SPL > $100 threshold.

## Decisions required before production
| Finding | Template treatment |
| --- | --- |
| Overview rounds weekly loads; walkthroughs use CEIL | Require `load_rounding` explicitly. Example chooses CEIL; ROUND is also implemented with half-up behavior. Neither is asserted as approved. |
| OnTrac narrative retains >30 lb with FedEx, but walkthrough describes all-weight OnTrac Zone 1 CPP | Require scenario CPP upstream to reflect the approved weight allocation. The example does not implement carrier weight routing. |
| RNO1→CBAK walkthrough lists 38,144 packages and 4,508 weekly volume with a divisor of 9 | Arithmetic does not reconcile: 38,144 / 9 ≈ 4,238.22. Do not use this walkthrough as a numeric golden test. |
| Historical walkthrough uses nine weeks | Set observation weeks explicitly for each analysis; do not infer all future windows have nine weeks. |
| MM conversion vs operating carrier mix | Conversion is a planning assumption; validate realized WMS allocation separately. |

## Comparison workbook contract
`BILL_WEIGHT_COMP` contains billable weight, volume, FedEx/OnTrac Zone 1 base+residential+fuel costs and CPP, and a CPP difference. Preserve this cost scope; these columns do not establish all-in savings including every surcharge or middle-mile cost.

`ZONE_WEIGHT_BAND_COMP` contains weight band, each carrier's from/to zones, volume, carrier CPPs, zone-switch EPP, and EPP delta. Distinguish each carrier's own zone-switch benefit from a direct FedEx-to-OnTrac package comparison. Aggregate CPPs with volume weighting. Recalculate from unrounded costs when available rather than treating rounded CPP differences as exact totals.
