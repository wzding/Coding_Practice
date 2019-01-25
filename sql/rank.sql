CREATE TABLE t (
    val INT
);
INSERT INTO t(val)
VALUES(1),(2),(2),(3),(4),(4),(5);

/*
row_number: Assigns a sequential integer to every row within its partition

dense_rank: Assigns a rank to every row within its partition based on the ORDER BY clause.
It assigns the same rank to the rows with equal values.
If two or more rows have the same rank, then there will be no gaps in the sequence of ranked values.

rank: Similar to the DENSE_RANK() function except that there are gaps in the
sequence of ranked values when two or more rows have the same rank.

PERCENT_RANK: is a window function that calculates the percentile rank of
a row within a partition or result set.
For a specified row, PERCENT_RANK() calculates the rank of that row minus one,
divided by 1 less than number of rows in the evaluated partition or query result set:
(rank - 1) / (total_rows - 1)
http://www.mysqltutorial.org/mysql-window-functions/mysql-percent_rank-function/

NTILE() function divides the rows in a sorted partition into a specific
number of groups. Each group is assigned an bucket number starting at one.
For each row, the NTILE() function returns a bucket number representing the
group to which the row belongs.
*/
-- DENSE_RANK
SELECT
    val,
    DENSE_RANK() OVER (
        ORDER BY val
    ) my_rank
FROM
    t;
-- RANK
SELECT
    val,
    RANK() OVER (
        ORDER BY val
    ) my_rank
FROM
    t;
-- NTILE
SELECT
    val,
    NTILE (4) OVER (
        ORDER BY val
    ) group
FROM
    t;

/*
Write a query that returns for each user on which day they became a power user.
That is, for each user, on which day they bought the 10th item.
*/
CREATE TABLE t (
    user_id INT NOT NULL,
    p_time TIMESTAMP NOT NULL
);

INSERT INTO t(user_id, p_time)
VALUES (1,'2014-10-31 16:16:12'),
(1,'2014-11-30 16:16:12'),
(1,'2014-12-30 16:16:12'),
(1,'2014-01-30 16:16:12'),
(1,'2014-02-24 16:16:12'),
(1,'2014-02-10 16:16:12'),
(2,'2014-12-30 16:16:12'),
(2,'2014-11-30 16:16:12'),
(2,'2014-09-30 16:16:12'),
(2,'2014-08-30 16:16:12'),
(3,'2014-10-30 16:16:12'),
(3,'2014-11-30 16:16:12'),
(3,'2014-12-30 16:16:12'),
(3,'2014-10-30 16:16:12'),
(3,'2014-01-30 16:16:12');

select user_id, p_time
from(
  select user_id, p_time,
  row_number() over (partition by user_id order by p_time) as row_num
from t
) tmp
where row_num = 3
