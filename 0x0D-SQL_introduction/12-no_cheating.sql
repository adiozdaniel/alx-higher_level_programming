-- This removes all records with a score <= 5
-- (in the second_table in my MySQL server).
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
