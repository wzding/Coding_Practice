/*
the minimum number of gold galleons needed to buy each non-evil wand of high power and age.
Write a query to print the id, age, coins_needed, and power of the wands that
Ron's interested in, sorted in order of descending power.
If more than one wand has same power, sort the result in order of descending age.
*/
select id, age, coins_needed, power
from Wands w
join Wands_Property p
on w.code = p.code
where p.is_evil = 0
and coins_needed = (
  select min(coins_needed)
  from Wands w1
  join Wands_Property p1
  on w1.code = p1.code
  where w1.power = w.power and p1.age = p.age
)
order by power desc, age desc
