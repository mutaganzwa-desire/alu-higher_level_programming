-- This script creates the table 'first_table' in the database 'hbtn_0c_0'
-- and then displays its full description using SHOW CREATE TABLE.

-- Step 1: Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(128) DEFAULT NULL,
    c CHAR(1) DEFAULT NULL,
    created_at DATE DEFAULT NULL,
    PRIMARY KEY (id)
);

-- Step 2: Display the full description of the table in the required form
SHOW CREATE TABLE first_table;
