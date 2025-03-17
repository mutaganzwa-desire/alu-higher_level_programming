-- This script lists all records from 'second_table' where the score >= 10, ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
