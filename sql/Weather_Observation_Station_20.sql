/*
A median is defined as a number separating the higher half of a data set from the lower half.
*/

SELECT ROUND(LAT_N, 4) from STATION s
WHERE (SELECT COUNT(*) FROM STATION WHERE LAT_N < s.LAT_N) =
  (SELECT COUNT(*) FROM STATION WHERE LAT_N > s.LAT_N)
