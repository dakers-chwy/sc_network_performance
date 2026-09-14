-- Synthetic failing fixture: returns SYNTH_A / 00001 / EXAMPLE with count 2.
-- Replace the fixture with the approved input/output; a clean result has zero rows.
WITH analysis_output AS (
    SELECT column1::VARCHAR AS package_id, column2::VARCHAR AS customer_zip5,
           column3::VARCHAR AS scenario_id
    FROM VALUES ('SYNTH_A', '00001', 'EXAMPLE'), ('SYNTH_A', '00001', 'EXAMPLE')
)
SELECT package_id, customer_zip5, scenario_id, COUNT(*) AS row_count
FROM analysis_output
GROUP BY package_id, customer_zip5, scenario_id
HAVING COUNT(*) > 1;
