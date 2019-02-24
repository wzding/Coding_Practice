/*
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
Write a query to output all such symmetric pairs in ascending order by the value of X
https://www.hackerrank.com/challenges/symmetric-pairs/problem
*/
-- easy to understand
(
    SELECT DISTINCT X, Y
    FROM Functions F3 WHERE X = Y
    group by X, Y
    having count(*) > 1
)
union
(
    select distinct f1.X, f1.Y
    from Functions f1
    join Functions f2
    on f1.x = f2.y and f1.y = f2.x and f1.x < f1.y
)
order by X

-- use EXISTS
(
  SELECT X, Y
  FROM Functions F1
  WHERE EXISTS(
    SELECT X,Y FROM Functions F2
    WHERE F1.X = F2.Y AND F1.Y = F2.X AND F1.X < F1.Y
  )
)
UNION
(
  SELECT DISTINCT X, Y
  FROM Functions F3 WHERE X = Y
  group by X, Y
  having count(*) > 1
)
ORDER BY X
