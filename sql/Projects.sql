/*
https://www.hackerrank.com/challenges/projects/problem
Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.
*/

/*
感觉这一种方法好理解一些
*/
set sql_mode = '';
-- can remove min because default is min if group by Start_Date
select
distinct a.Start_Date, min(b.End_Date)
from
Projects a,
Projects b
where a.Start_Date not in (select End_Date from Projects)
and b.End_Date not in (select Start_Date from Projects)
and a.Start_Date < b.End_Date
group by a.Start_Date
order by datediff(b.End_Date, a.Start_Date), a.Start_Date;


SET sql_mode = '';
-- can remove min because default is min if group by Start_Date
SELECT Start_Date, MIN(End_Date)
from
(SELECT Start_Date FROM Projects
      WHERE Start_Date NOT IN (SELECT DISTINCT End_Date FROM Projects)) a,
(SELECT End_Date FROM Projects
      WHERE End_Date NOT IN (SELECT DISTINCT Start_Date FROM Projects)) b
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY datediff(End_Date, Start_Date), Start_Date;
