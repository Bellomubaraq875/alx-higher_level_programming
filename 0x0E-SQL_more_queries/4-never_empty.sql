-- This script creates a table whose database name is pasd as an argument
-- on the comand line
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256));
