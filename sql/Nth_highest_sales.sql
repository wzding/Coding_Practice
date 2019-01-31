create table sales_table (
  productid INT,
  sale INT
);

insert into sales_table (productid, sale) values
  (1, 4),
  (2, 3),
  (6, 9),
  (7, 7),
  (8, 4);
/*
2nd highest sale
*/
select max(sale) as second_highest_sale
from sales
where sale < (select max(sale) from sales)
-- use offset note that need to use another select
select (
select distinct sale
from sales
order by sale desc
limit 1 offset 1) as second_highest_sale;
/*
kth highest sale --> kth higest means there are k unique numbers that less or equal to this number
*/
select distinct sale from sales s1
where 2 = (select count(distinct sale) from sales s2 where s1.sale <= s2.sale)
/*
kth highest sale
*/
select sale from
(select distinct sale from sales order by sale desc limit 5) as s
order by sale
limit 1
-- use a function
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct Salary from Employee
      order by Salary desc
      limit 1 offset N
  );
END
--- use nth_value
select nth_value(sale, 3) over (order by sale desc) as nth
from sales_table
order by nth desc
limit 1
