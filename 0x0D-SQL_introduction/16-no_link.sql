--  lists all records of the table second_table of the database
-- Records are listed by descending score
SELECT score, name
FROM second_table
WHERE `name` != ""
ORDER BY score DESC;
