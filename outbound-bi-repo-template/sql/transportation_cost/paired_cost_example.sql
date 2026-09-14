-- Synthetic Snowflake example; one row per package per scenario.
-- Missing costs stay missing; zero cost is not considered missing.
WITH ratings AS (
    SELECT column1::VARCHAR AS package_id,
           column2::NUMBER(18,4) AS baseline_cost,
           column3::NUMBER(18,4) AS scenario_cost
    FROM VALUES ('SYNTH_A', 7.00, 5.00), ('SYNTH_B', 6.00, 7.00),
                ('SYNTH_C', NULL, 5.00), ('SYNTH_D', 0.00, 0.00)
), classified AS (
    SELECT *, baseline_cost IS NOT NULL AND scenario_cost IS NOT NULL AS paired
    FROM ratings
)
SELECT COUNT(*) AS eligible_packages,
       COUNT_IF(paired) AS paired_packages,
       COUNT_IF(baseline_cost IS NULL) AS missing_baseline_packages,
       COUNT_IF(scenario_cost IS NULL) AS missing_scenario_packages,
       COUNT_IF(baseline_cost IS NULL AND scenario_cost IS NULL) AS both_missing_packages,
       COUNT_IF(paired) / NULLIF(COUNT(*), 0)::FLOAT AS paired_coverage,
       SUM(IFF(paired, baseline_cost, NULL)) / NULLIF(COUNT_IF(paired), 0) AS baseline_cpp,
       SUM(IFF(paired, scenario_cost, NULL)) / NULLIF(COUNT_IF(paired), 0) AS scenario_cpp,
       SUM(IFF(paired, baseline_cost - scenario_cost, NULL)) AS gross_entitlement,
       SUM(IFF(paired, baseline_cost - scenario_cost, NULL)) / NULLIF(COUNT_IF(paired), 0) AS epp
FROM classified;
