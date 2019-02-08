/*
A median is defined as a number separating the higher half of a data set from the lower half.
https://www.hackerrank.com/challenges/weather-observation-station-20/problem
*/
-- mysql
SELECT ROUND(LAT_N, 4) from STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N) =
  (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N)

-- mysql server
select CAST(avg(LAT_N) AS DECIMAL(10,4))
from (
    select LAT_N,
    row_number() over (order by LAT_N) as row_a,
    row_number() over (order by LAT_N desc) as row_b
    from STATION
) tmp
where row_a between row_b - 1 and row_b + 1
