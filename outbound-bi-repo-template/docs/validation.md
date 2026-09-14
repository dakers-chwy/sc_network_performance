# Analytical validation

## Before interpretation
Record run ID, commit, scenario config, reporting timezone, date window, source snapshots, package key, and freshness. Confirm one-to-one/one-to-many join expectations before enrichment.

## Required evidence
- Count input packages, excluded packages by reason, retained packages, paired packages, and unrated packages.
- Reconcile duplicate keys and pre/post-join counts at the declared grain.
- Assert that totals use a common rating population; retain zero cost as valid when supported.
- Reconcile component cost to total cost and gross entitlement to net savings.
- Validate dates around midnight, overnight CPT, weekends, missing EDD, and late no-POD.
- For allocation, separate eligibility loss from cost/service selection and compare modeled vs observed assignments.
- For dedicated costs, ensure multiple SCACs or shipment versions do not repeat route package volume.

## What the included checks prove
Local unit tests cover the synthetic lane calculator's economics, load rounding, threshold boundary, and invalid inputs. They do not validate carrier rate tables, Snowflake permissions, production SQL compilation, source freshness, or WMS behavior. Run SQL starters in a development worksheet before adapting them.
