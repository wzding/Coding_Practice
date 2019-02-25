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
That is, for each user, on which day they bought the 3rd item.
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
from (
  select user_id, p_time,
  row_number() over (partition by user_id order by p_time) as row_num
  from t
) tmp
where row_num = 3

/*
find out top 3 product in each category in terms of sales on a daily basis

partion by used in window function is different from group by
https://stackoverflow.com/questions/2404565/sql-server-difference-between-partition-by-and-group-by
top k products -- return exact k rows

top products with top k distinct sales numbers --> change ROW_NUMBER to dense_rank
dense_rank generates the same rank number when the sales number is the same
*/
create table sales_table (
  productid int,
  productname char(50),
  sales int,
  salesdate date,
  category char(20)
);
insert into sales_table (productid, productname, sales, salesdate, category)
  values
  (1, 'jeans1', 10, "2018-01-01", 'cloth'),
  (2, 'top1', 10, "2018-01-01", 'cloth'),
  (3, 'dress1', 20, "2018-01-01", 'cloth'),
  (4, 'short1', 30, "2018-01-01", 'cloth'),
  (5, 'shoe1', 100, "2018-01-01", 'shoe'),
  (11, 'jeans2', 1, "2018-02-01", 'cloth'),
  (12, 'top2', 100, "2018-02-01", 'cloth'),
  (11, 'dress2', 210, "2018-02-01", 'cloth'),
  (14, 'short2', 30, "2018-02-01", 'cloth'),
  (15, 'shoe2', 50, "2018-02-01", 'shoe'),
  (21, 'jeans3', 20, "2018-03-01", 'cloth'),
  (22, 'top3', 70, "2018-03-01", 'cloth'),
  (23, 'dress3', 30, "2018-03-01", 'cloth'),
  (24, 'short3', 30, "2018-03-01", 'cloth'),
  (25, 'shoe3', 80, "2018-03-01", 'shoe'),
  (31, 'jeans4', 60, "2018-04-01", 'cloth'),
  (32, 'top4', 44, "2018-04-01", 'cloth'),
  (33, 'dress4', 220, "2018-04-01", 'cloth'),
  (34, 'short4', 530, "2018-04-01", 'cloth'),
  (35, 'shoe4', 600, "2018-04-01", 'shoe');

select category, salesdate, productname, productid, sales_rank, sales
from (
  select *,
  row_number() over(
    partition by salesdate, category
    order by sales desc) as sales_rank
  from sales_table) tmp
where row_num <= 3
order by category, salesdate, sales_rank
