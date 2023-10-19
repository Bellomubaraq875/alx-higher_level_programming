-- This script creates a table on the server
-- The database name is passed as an argument on the comand line
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
