-- This script lists the number of records for each score in 'second_table' and sorts by the number of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
