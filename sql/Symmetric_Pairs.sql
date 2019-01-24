/*
Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

Write a query to output all such symmetric pairs in ascending order by the value of X
*/
(SELECT X, Y
FROM Functions F1
WHERE EXISTS(
    SELECT X,Y FROM Functions F2
    WHERE F1.X = F2.Y AND F1.Y = F2.X AND F1.X < F1.Y))
UNION
(SELECT DISTINCT X, Y
FROM Functions F3 WHERE X = Y AND (
    SELECT COUNT(*) FROM Functions
    WHERE Functions.X = F3.X AND Functions.Y = F3.Y) > 1)
ORDER BY X
