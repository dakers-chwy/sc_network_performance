-- Synthetic date-level example. Convert actual timestamps before supplying dates.
WITH packages AS (
    SELECT column1::VARCHAR AS package_id, column2::DATE AS edd,
           column3::DATE AS delivered_date, column4::DATE AS as_of_date
    FROM VALUES
      ('SYNTH_A', '2026-09-10', '2026-09-10', '2026-09-14'),
      ('SYNTH_B', '2026-09-10', NULL, '2026-09-14'),
      ('SYNTH_C', '2026-09-14', NULL, '2026-09-14'),
      ('SYNTH_D', NULL, NULL, '2026-09-14')
)
SELECT *, CASE
    WHEN edd IS NULL THEN 'Missing EDD'
    WHEN delivered_date IS NULL AND as_of_date > edd THEN 'Late - No POD'
    WHEN delivered_date IS NULL THEN 'No POD'
    WHEN delivered_date < edd THEN 'Early'
    WHEN delivered_date = edd THEN 'On Time'
    ELSE 'Late'
END AS service_bucket
FROM packages;
