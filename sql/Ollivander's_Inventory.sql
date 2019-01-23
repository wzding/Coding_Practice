/*
the minimum number of gold galleons needed to buy each non-evil wand of high power and age.
Write a query to print the id, age, coins_needed, and power of the wands that
Ron's interested in, sorted in order of descending power.
If more than one wand has same power, sort the result in order of descending age.
*/
SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W
INNER JOIN Wands_Property P
ON W.code = P.code
WHERE P.is_evil = 0 AND
W.coins_needed = (
    SELECT MIN(Wands.coins_needed) FROM
    Wands INNER JOIN Wands_Property
    ON Wands.code = Wands_Property.code
    WHERE Wands.power = W.power and Wands_Property.age = P.age
)
ORDER BY W.power DESC, P.age DESC
