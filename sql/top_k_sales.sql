/*
partion by used in window function is different from group by
https://stackoverflow.com/questions/2404565/sql-server-difference-between-partition-by-and-group-by

NOTE this is for sql server NOT MySQL
top k products -- return exact k rows
*/
with r as (
  select
  Category,
  ProductID,
  ProductName,
  SalesDate,
  Sales,
  ROW_NUMBER() over (partition by
    Category,
    SalesDate,
    order by sales desc) AS Sales_Rank
  from product_sales
)
select s.Category,
s.SalesDate,
s.ProductID,
s.ProductName,
r.Sales_Rank,
r.Sales from product_sales s inner join r
on s.ProductID = r.ProductID and s.SalesDate = r.SalesDate
where r.Sales_Rank <= 3
order by s.Category, s.SalesDate, r.Sales_Rank

/*
top products with top k distinct sales numbers --> change ROW_NUMBER to dense_rank
dense_rank generates the same rank number when the sales number is the same
*/
with r as (
  select
  Category,
  ProductID,
  ProductName,
  SalesDate,
  Sales,
  dense_rank() over (partition by
    Category,
    SalesDate,
    order by sales desc) AS Sales_Rank
  from product_sales
)

select s.Category,
s.SalesDate,
s.ProductID,
s.ProductName,
r.Sales_Rank,
r.Sales from product_sales s inner join r
on s.ProductID = r.ProductID and s.SalesDate = r.SalesDate
where r.Sales_Rank <= 3
order by s.Category, s.SalesDate, r.Sales_Rank
