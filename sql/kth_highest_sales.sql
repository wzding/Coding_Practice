/*
2nd highest sale
*/
select max(sale) as second_highest_sale
from sales
where sale < (select max(sale) from sales)

/*
kth highest sale --> kth higest means there are k unique numbers that less or equal to this number
*/
select distinct sale from sales s1
where 2 = (select count(distinct sale) from sales s2 where s1.sale <= s2.sale)

/*
kth highest sale
*/
select sale from
(select distinct sale from sales order by sale desc limit 2) as s
order by sale
limit 1
