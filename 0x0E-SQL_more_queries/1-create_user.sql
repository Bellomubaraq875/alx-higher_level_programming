-- This script creates the MySQL server user specified
-- It grants the user all privileges, and sets the password
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1;
