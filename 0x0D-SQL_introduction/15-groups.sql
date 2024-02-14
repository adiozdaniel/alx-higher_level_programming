-- This lists all records of the table second_table
-- (having a name value in my MySQL server)
-- Records are ordered by descending score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

