/*
The total score of a hacker is the sum of their maximum scores for all of the challenges.

Write a query to print the hacker_id, name, and total score of the hackers
ordered by the descending score. If more than one hacker achieved the same
total score, then sort the result by ascending hacker_id. Exclude all hackers
with a total score of 0 from your result.
https://www.hackerrank.com/challenges/contest-leaderboard/problem

注意先join 再having 最后order
*/
SELECT H.hacker_id, H.name, SUM(S.maxscore) AS total
FROM Hackers H
INNER JOIN (
    SELECT hacker_id, MAX(score) as maxscore
    from Submissions
    GROUP BY hacker_id, challenge_id
) S
ON H.hacker_id = S.hacker_id
GROUP BY H.hacker_id, H.name
HAVING total > 0
ORDER BY total DESC, H.hacker_id
