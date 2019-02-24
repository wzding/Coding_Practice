/*
Write a query to find the maximum total earnings for all employees as well as
the total number of employees who have maximum total earnings.
where months * salary = (select max(months * salary) from Employee)
group by total
https://www.hackerrank.com/challenges/earnings-of-employees/problem
*/
select months * salary as total, count(*)
from Employee
where months * salary = (select max(months * salary) from Employee)
group by total


select salary * months as total, count(*)
from Employee
group by total
order by total desc limit 1;
