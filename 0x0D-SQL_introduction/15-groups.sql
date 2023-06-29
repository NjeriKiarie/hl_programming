-- a script that lists the number of records with the same score in the second_table of database hbtn_0c_0
-- the result should deisplay the score and the number of records for this score with the label number
-- the list should be sorted by the number of records(descendingz)
-- the database neme will be passed as an argument to the mysql command


SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
