-- Synthetic Snowflake example: Saturday week ending independent of WEEK_START.
WITH dates AS (
    SELECT column1::DATE AS reporting_date
    FROM VALUES ('2026-09-12'), ('2026-09-13'), ('2026-09-14')
)
SELECT reporting_date,
       DATEADD(DAY, MOD(6 - DAYOFWEEKISO(reporting_date) + 7, 7), reporting_date)::DATE AS weekending_date
FROM dates
ORDER BY reporting_date;
