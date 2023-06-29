-- A script that  lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server
-- Dont list rows without a name value
-- Results should display the score and the name (in this oreder)
-- Records should be listed by descending scor
-- The database name will be passed as an argument to the mysqlcommand

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
