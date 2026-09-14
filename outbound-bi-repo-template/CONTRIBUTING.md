# Contribution workflow

Start with the business question and output grain. A reusable query belongs under its domain; a dated investigation belongs in `projects/`. Keep business rules in one documented location and reference them from downstream work.

1. Create a feature, fix, analysis, or documentation branch.
2. State input tables, joins, filters, date boundaries, and intended output.
3. Use explicit columns, named CTEs, and meaningful aliases. Deduplicate before many-to-one mapping joins; document the deterministic winner.
4. Validate grain, match coverage, exclusions, denominators, and cost reconciliation.
5. Attach aggregate evidence to the PR and record any remaining limitations.
6. Obtain the team's normal review before merging. Schedule and deploy warehouse changes through the existing operational process.

For SQL changes, record warehouse, role, execution date, query IDs, row counts, and sample cases. A local Python pass does not validate Snowflake SQL.

Name SQL files by execution order where order matters, for example `10_population.sql`, `20_eligibility.sql`, `30_rating.sql`, `40_output.sql`. Include scenario and effective-date identifiers in outputs, not hardcoded file names for every rerun.
