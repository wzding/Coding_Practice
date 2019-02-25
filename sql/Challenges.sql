/*
https://www.hackerrank.com/challenges/challenges/problem
print the hacker_id, name, and the total number of challenges created by each student.

If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.
*/
select h.hacker_id, h.name, count(c.challenge_id) as total
from Challenges c
join Hackers h
on c.hacker_id = h.hacker_id
group by h.hacker_id, h.name
having total = (
    select count(*)
    from Challenges
    group by hacker_id
    order by count(*) desc
    limit 1
)
or total in (
    select cnt
    from (
      select count(challenge_id) as cnt
      from Challenges
      group by hacker_id
    ) tmp
    group by cnt
    having count(cnt) = 1
  )
order by total desc, h.hacker_id


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
    select cnt
    from (
      select count(challenge_id) as cnt
      from Challenges
      group by hacker_id
    ) tmp
    group by cnt
    having count(cnt) = 1
  )
order by total desc, h.hacker_id
