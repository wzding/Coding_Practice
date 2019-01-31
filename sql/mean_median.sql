/*
Find the average and median transaction amount only considering those
transactions that happen on the same date as that user signed-up.
*/
CREATE TABLE user (
    user_id INT NOT NULL,
    sign_up_date DATE NOT NULL
);

INSERT INTO user(user_id, sign_up_date)
VALUES (1,'2014-03-30'),
(2,'2014-01-30'),
(3,'2014-02-10'),
(4,'2014-05-30');

CREATE TABLE transaction_table (
    user_id INT NOT NULL,
    transaction_date TIMESTAMP NOT NULL,
    transaction_amount INT NOT NULL
);
INSERT INTO transaction_table(user_id, transaction_date, transaction_amount)
VALUES (1,'2014-03-30 00:00:00', 15),
(1,'2014-04-30 00:00:00', 30),
(1,'2014-03-30 01:00:00', 20),
(2,'2014-01-30 01:00:00', 2),
(2,'2014-01-30 02:00:00', 6),
(3,'2014-02-10 00:00:00', 4),
(4,'2014-05-30 00:00:00', 3);
-- get median
SELECT AVG(transaction_amount) AS mean,
  AVG(
    CASE WHEN row_a BETWEEN row_b - 1 AND row_b + 1
    THEN transaction_amount ELSE NULL END
  ) AS median
FROM (
  SELECT transaction_amount,
  ROW_NUMBER() OVER(ORDER BY transaction_amount) AS row_a,
  ROW_NUMBER() OVER(ORDER BY transaction_amount DESC) AS row_b
  FROM transaction_table
  JOIN user
  ON transaction_table.user_id = user.user_id AND
  DATE(transaction_table.transaction_date) = user.sign_up_date
) tmp;

/*
知道frequency 并不是单独的数字
不用 window functions
必须 consider previous cumulative frequency
https://leetcode.com/problems/find-median-given-frequency-of-numbers/
*/
CREATE TABLE numbers (
    number INT NOT NULL,
    frequency INT NOT NULL
);

INSERT INTO numbers(number, frequency)
VALUES (0,7),
(1,1),
(2,3),
(3,1);

select avg(number) as median
from (
    select *,
    @prev := @curr as prev,
    @curr := @prev + frequency as curr,
    (select sum(frequency) from numbers) as total
    from numbers,
    (select @curr := 0, @prev := 0) init
    order by number
) tmp
where curr >= floor((total+1)/2)
and prev <= total - floor((total+1)/2)

/*
延伸一下 求 median salary at each company
https://leetcode.com/problems/median-employee-salary/
*/
select Id, tmp.Company, Salary
from (
    select *,
    @curr := if(@prev = Company, @curr := @curr + 1, 1) as rank_num,
    @prev := Company
    from
    Employee,
    (select @curr := 1, @prev := Null) init
    order by Company, Salary
) tmp
left join
(select Company,
 count(*) as total
 from Employee
 group by Company
) cnt
on tmp.Company = cnt.Company
where total % 2 = 0 and rank_num between total / 2 and total / 2 + 1
or total % 2 = 1 and rank_num = (total + 1) / 2
