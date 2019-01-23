/*
https://www.hackerrank.com/challenges/challenges/problem
print the hacker_id, name, and the total number of challenges created by each student.

If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.
*/
SELECT H.hacker_id, H.name, COUNT(*) AS total
FROM Hackers H
INNER JOIN Challenges C
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING total = (
    SELECT COUNT(*) as cnt1
    FROM Challenges
    GROUP BY hacker_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
or total in (
    SELECT DISTINCT cnt2 FROM (
        SELECT COUNT(*) AS cnt2
        FROM Hackers
        INNER JOIN Challenges
        ON Hackers.hacker_id = Challenges.hacker_id
        GROUP BY Hackers.hacker_id, Hackers.name
    ) cnt_table
    GROUP BY cnt2
    HAVING COUNT(cnt2) = 1
)
ORDER BY total DESC, H.hacker_id

--- change how to choose max
SELECT H.hacker_id, H.name, COUNT(*) AS total
FROM Hackers H
INNER JOIN Challenges C
ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING total = (
    SELECT max(cnt1)
    from (
        SELECT count(*) as cnt1
        FROM Challenges
        GROUP BY hacker_id
    ) temp
)
or total in (
    SELECT DISTINCT cnt2 FROM (
        SELECT COUNT(*) AS cnt2
        FROM Hackers
        INNER JOIN Challenges
        ON Hackers.hacker_id = Challenges.hacker_id
        GROUP BY Hackers.hacker_id, Hackers.name
    ) cnt_table
    GROUP BY cnt2
    HAVING COUNT(cnt2) = 1
)
ORDER BY total DESC, H.hacker_id
