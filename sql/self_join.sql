/*
https://sqlzoo.net/wiki/Self_join
*/
-- 9. Give a distinct list of the stops which may be reached from
-- 'Craiglockhart' by taking one bus. Include the company and bus no. of the
-- relevant services.
SELECT distinct stops.name, a.company, a.num
FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
JOIN stops ON a.stop = stops.id
WHERE b.stop = (select id from stops where name = 'Craiglockhart')
and a.company = 'LRT'

-- 10. Find the routes involving two buses that can go from Craiglockhart to Sighthill.
-- Show the bus no. and company for the first bus, the name of the stop for the transfer,
-- and the bus no. and company for the second bus.
-- HINT: Self-join twice to find buses that visit Craiglockhart and Sighthill, then
-- join those on matching stops.
select
a.num, a.company, stops.name, c.num, c.company
from route a
join route b
on a.company = b.company and a.num = b.num
join stops
on b.stop = stops.id
join (route c join route d
on c.company = d.company and c.num = d.num)
where a.stop = (select id from stops where name = 'Craiglockhart')
and d.stop = (select id from stops where name = 'Lochend')
and b.stop = c.stop
