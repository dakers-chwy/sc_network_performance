# Business rules and scenario boundaries

These are starting conventions from supplied project context. Confirm effective dates and implementation against approved production code before migration.

| Area | Rule / required treatment |
| --- | --- |
| Reporting time | Eastern reporting; convert timestamps according to the actual source timestamp type before taking DATE |
| Week | Sunday through Saturday; use the ISO-based example to avoid session WEEK_START differences |
| Core | Retail + Freezer for the current general Core scope; historical RFP population must be verified separately |
| LOB | Keep Rx, Fresh, CFS, SmartPak, and Drop Ship identifiable; inclusion is scenario-specific |
| Package grain | Declare the source key; service detail commonly uses tracking number + customer ZIP5; add scenario/candidate/rate keys for what-if comparisons |
| DEA | On time means delivery date <= applicable EDD; distinguish missing EDD from missing POD |
| No POD | Missing delivery after EDD is Late - No POD; on/before EDD is No POD |
| Padding | Padded and unpadded EDD measures remain separate; document manual/automated/overlap and FC_CLOSED treatment |
| Routing | Eligible station ZIP coverage is an opportunity ceiling, not a WMS allocation prediction |
| CPT | Record source timezone and operating date; overnight cutoff ownership and missing/failed parsing must be explicit |
| FedEx mapping | Normalize co-located master/ground stations before joining demand to candidate stations |
| OnTrac mapping | Zone 1 additions preserve non-Zone-1 alternatives; avoid multiplying packages across alternatives |
| Dedicated | Context SCAC seed: USAD, SNCY, WEND, BGES, HTSH, HHTD; confirm LGED and effective dates before adoption |
| Middle mile | Use OTM shipment detail for dedicated classification, with package-FC to rate-FC bridge and FC-route-week grain |
| FC bridge | Context exceptions CFF1→CFC1, RNF1→RNO1; store approved mappings explicitly and effective-date them |
| RFP | Retain candidate exclusions before CPP; distinguish gross entitlement from net savings after MM cost |
| Cost | Compare identical packages, weights, service assumptions, and rate-effective dates; preserve unrated reasons |

A blanket 02:00 cutoff adjustment, nearest-station assumption, or carrier coverage assumption is not a production routing rule. Preserve decision reasons and reconcile them against observed WMS assignments.
