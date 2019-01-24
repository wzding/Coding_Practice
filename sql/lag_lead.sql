/*
LAG: Returns the value of the Nth row before the current row in a partition.
It returns NULL if no preceding row exists.

LAG(<expression>[,offset[, default_value]]) OVER (
    PARTITION BY expr,...
    ORDER BY expr [ASC|DESC],...
)

LEAD: Returns the value of the Nth row after the current row in a partition.
It returns NULL if no subsequent row exists.

LEAD(<expression>[,offset[, default_value]]) OVER (
    PARTITION BY (expr)
    ORDER BY (expr)
)
*/

WITH productline_sales AS (
    SELECT productline,
           YEAR(orderDate) order_year,
           ROUND(SUM(quantityOrdered * priceEach),0) order_value
    FROM orders
    INNER JOIN orderdetails USING (orderNumber)
    INNER JOIN products USING (productCode)
    GROUP BY productline, order_year
)
-- lag
SELECT
    productline,
    order_year,
    order_value,
    LAG(order_value, 1) OVER (
        PARTITION BY productLine
        ORDER BY order_year
    ) prev_year_order_value
FROM
    productline_sales;
-- lead
SELECT
    customerName,
    orderDate,
    LEAD(orderDate, 1) OVER (
        PARTITION BY customerNumber
        ORDER BY orderDate ) nextOrderDate
FROM
    orders
INNER JOIN customers USING (customerNumber);

/*
例题
For each user_id, find the difference between the last action and the second
last action. Action here is defined as visiting a page. If the user has just
one action, you can either remove her from the final results or keep that
user_id and have NULL as time difference between the two actions.

The table below shows for each user all the pages she visited and the corresponding timestamp.
Column  |   Name  |  Value Description
user_id | 6684 |  this is id of the user
page  |  home_page |  the page visited
unix_timestamp |  1451640067 |  unix timestamp in seconds
*/
select user_id,
  unix_timestamp - previous_timestamp
from (
  select user_id,
  unix_timestamp,
  lag(unix_timestamp, 1) over (
    partition by user_id order by unix_timestamp) as previous_timestamp,
  row_number() over (
    partition by user_id order by unix_timestamp desc) as row,
  from table) temp
where row = 1
group by user_id
