/*
two month data get sum and cum sum
*/
CREATE TABLE march (
    user_id INT NOT NULL,
    p_date DATE NOT NULL,
    transaction_amount INT NOT NULL
);
INSERT INTO march(user_id, p_date, transaction_amount)
VALUES (1,'2014-03-31', 15),
(1,'2014-03-30', 30),
(1,'2014-03-30', 20),
(1,'2014-03-30', 1),
(1,'2014-03-24', 2),
(1,'2014-03-10', 6),
(2,'2014-03-30', 4),
(2,'2014-03-30', 3),
(2,'2014-03-30', 2),
(2,'2014-03-30', 4),
(3,'2014-03-30', 6),
(3,'2014-03-30', 8),
(3,'2014-03-30', 8),
(3,'2014-03-30', 6),
(3,'2014-03-30', 2);

CREATE TABLE april (
    user_id INT NOT NULL,
    p_date DATE NOT NULL,
    transaction_amount INT NOT NULL
);
INSERT INTO april(user_id, p_date, transaction_amount)
VALUES (1,'2014-10-31', 15),
(1,'2014-04-30', 30),
(1,'2014-04-30', 20),
(1,'2014-04-30', 1),
(1,'2014-04-24', 2),
(1,'2014-04-10', 6),
(12,'2014-04-30', 4),
(12,'2014-04-30', 3),
(12,'2014-04-30', 2),
(12,'2014-04-30', 4),
(13,'2014-04-30', 6),
(13,'2014-04-30', 8),
(13,'2014-04-30', 8),
(13,'2014-04-30', 6),
(13,'2014-04-30', 2);
/*
Write a query that returns the total amount of money spent by each user.
That is, the sum of the column transaction_amount for each user over both tables.
注意一定要 union all
*/
SELECT user_id, SUM(transaction_amount) as s
from (
  (SELECT * FROM march)
  UNION ALL
  (SELECT * FROM april)
) all_data
GROUP BY user_id
-- +---------+-------------------------+
-- | user_id | sum(transaction_amount) |
-- +---------+-------------------------+
-- |       1 |                     148 |
-- |       2 |                      13 |
-- |       3 |                      30 |
-- |      12 |                      13 |
-- |      13 |                      30 |
-- +---------+-------------------------+

/*
returns day by day the cumulative sum of money spent by each user. That is,
each day a user had a transcation, we should have how much money she has
spent in total until that day.
注意要使用 distinct 否则结果有重复
*/
select distinct user_id,
p_date,
sum(transaction_amount) over(partition by user_id order by p_date) as cum_sum
from (
  (select * from march)
  union all
  (select * from april)
) march_april
order by user_id, p_date;
-- +---------+------------+---------+
-- | user_id | p_date     | cum_sum |
-- +---------+------------+---------+
-- |       1 | 2014-03-10 |       6 |
-- |       1 | 2014-03-24 |       8 |
-- |       1 | 2014-03-30 |      59 |
-- |       1 | 2014-03-31 |      74 |
-- |       1 | 2014-04-10 |      80 |
-- |       1 | 2014-04-24 |      82 |
-- |       1 | 2014-04-30 |     133 |
-- |       1 | 2014-10-31 |     148 |
-- |       2 | 2014-03-30 |      13 |
-- |       3 | 2014-03-30 |      30 |
-- |      12 | 2014-04-30 |      13 |
-- |      13 | 2014-04-30 |      30 |
-- +---------+------------+---------+

/*
 get the cumulative sum of an employee's salary over a period of 3 months
 but exclude the most recent month.
Find Cumulative Salary of an Employee
https://leetcode.com/problems/find-cumulative-salary-of-an-employee/
*/
select
e1.Id,
e1.Month,
ifnull(e1.Salary, 0) + ifnull(e2.Salary, 0) + ifnull(e3.Salary, 0) as Salary
from Employee e1
left join Employee e2
-- last month
on e1.Id = e2.Id and e1.Month = e2.Month + 1
left join Employee e3
-- month before last month
on e1.Id = e3.Id and e1.Month = e3.Month + 2
-- remove most recent month
where (e1.Id, e1.Month) not in
(select Id, max(Month) from Employee group by Id)
order by Id, Month desc;
