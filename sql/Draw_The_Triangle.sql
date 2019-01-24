/*
https://www.hackerrank.com/challenges/draw-the-triangle-1/problem
print the pattern below
* * * * *
* * * *
* * *
* *
*

*/
SET @count := 21;
SELECT repeat('* ', @count := @count - 1)
from information_schema.tables
limit 20

--- or like this
SELECT repeat('* ', @count := @count - 1)
from information_schema.tables,
(SELECT @count := 21) init
limit 20
