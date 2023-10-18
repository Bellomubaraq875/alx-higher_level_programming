-- This script converts a database to UTf8
-- ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4_unicode_ci;
USE hbtn_0c_;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
