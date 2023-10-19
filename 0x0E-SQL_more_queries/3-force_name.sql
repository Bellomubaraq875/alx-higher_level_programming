-- This script creates a table on my server
-- The database name will be passed as an argument on the mysql command
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL);
