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
each day a user had a transcation, we should have how much money she has spent in total until that day.
*/

SELECT user_id,
  p_date,
  SUM(amount) over (
    partition by user_id order by p_date
  ) as total
FROM
(
  (SELECT user_id, p_date,
   sum(transaction_amount) as amount
   FROM march
    group by user_id, p_date)
  UNION ALL
  (SELECT user_id, p_date,
   sum(transaction_amount) as amount
   FROM april
   group by user_id, p_date)
) all_data
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
