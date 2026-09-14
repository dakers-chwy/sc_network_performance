# Source catalog

Candidate integrations from existing project context; schemas, privileges, freshness, and keys must be verified in Snowflake. This template has no live connection.

| Source | Intended use | Key validation |
| --- | --- | --- |
| EDLDB.CHEWYBI.SHIPMENT_TRANSACTIONS | Package demand and shipment attributes | Dedup winner, package key, timestamp types |
| EDLDB.BT_SC_TRANSPORTATION.CARRIER_TRACKING_EVENTS | Induction, OFD, delivery, first physical stop | Repeated events, carrier+tracking match, event/ingestion latency |
| EDLDB.CHEWYBI.LITE_OUTBOUND_SHIPMENT_DETAIL | OTM lane, SCAC, shipment cost context | Version dedup and FC-route-week fanout |
| EDLDB.CHEWYBI.COMMON_DATE | Financial periods | One row per date and period alignment |
| EDLDB.CHEWYBI.SHIPROUTE | FC-route coverage | Active route, effective dates, duplicate ZIP mappings |
| EDLDB.SRM.SRM_FDX_REF_COV_BASE | FedEx ZIP-to-master station coverage | Snapshot date and canonical station mapping |
| EDLDB.SRM.SRM_FDX_REF_TERM_MASTER_BASE | Station metadata | Station ID normalization |
| EDLDB.SC_OPERATIONS_SANDBOX.FEDEX_CO_LOCATIONS_MAPPING | Co-location bridge | One approved canonical mapping per effective date |
| EDLDB.SC_OPERATIONS_SANDBOX.ONTRAC_ZONE_MAPPING | OnTrac route/ZIP/zone options | Preserve alternatives; explicit scenario selection |
| EDLDB.WIZMO.WIZMO_EDD_HISTORY | Promise history and constraints | Request selection and constraint timing |
| EDLDB.SC_PROMISE_SANDBOX.EDD_CONTINGENCY_PADDING | Padding windows and reasons | Time/ZIP/FC overlap |
| EDLDB.SC_OPERATIONS_SANDBOX.OBP_PACKAGE_SERVICE_DETAIL | Service reporting output | Tracking+ZIP grain and refresh completeness |
| EDLDB.SC_OPERATIONS_SANDBOX.OBP_OUTBOUND_TRANSPORTATION_COST_ESTIMATES | Benchmark costs | Package/date key, rate version and component completeness |

For each production adoption, add owner, refresh SLA, warehouse, role, source timestamp, snapshot date, column contract, upstream job, and downstream consumers.
