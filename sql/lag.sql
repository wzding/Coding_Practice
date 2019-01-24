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
