# Lane economics input contract

One row per `scenario_id + fc + lane`. All costs are USD. Inputs describe retained, rated packages; upstream unmatched coverage must be reported separately.

| Column | Meaning |
| --- | --- |
| scenario_id | Scenario/version identifier |
| fc | Rating FC |
| lane | Candidate lane identifier |
| retained_packages | Nonnegative integer package count in the observation window |
| baseline_cpp | Nonnegative cost per package for the retained comparison population |
| scenario_cpp | Nonnegative scenario CPP for exactly the same population |
| cpl_no_fsc | Middle-mile cost/load excluding fuel |
| min_miles | Nonnegative mileage on the same procurement basis as fuel/mile |

The calculator applies conversion uniformly to package demand and entitlement. If weights or carrier allocation change CPP under conversion, calculate the adjusted CPP upstream. Zero volume produces zero loads and no candidate, overriding the positive-volume minimum-load assumption. Economic eligibility does not imply service or launch approval.

Output includes weekly/converted volume, loads, gross entitlement, MM cost, net savings, SPL, and an economic threshold flag. Configuration holds observation weeks and the historical modeling assumptions explicitly.
