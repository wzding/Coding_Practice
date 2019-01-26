/*
find out top 3 product in each category in terms of sales on a daily basis

partion by used in window function is different from group by
https://stackoverflow.com/questions/2404565/sql-server-difference-between-partition-by-and-group-by
top k products -- return exact k rows
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

/*
top products with top k distinct sales numbers --> change ROW_NUMBER to dense_rank
dense_rank generates the same rank number when the sales number is the same
*/
