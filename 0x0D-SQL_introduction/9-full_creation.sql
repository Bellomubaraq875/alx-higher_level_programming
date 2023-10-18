-- This script creates another table in the database
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Insery the data into the table
INSERT INTO second_table(id, name, score) VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8)
;
