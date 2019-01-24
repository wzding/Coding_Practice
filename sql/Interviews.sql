/*
https://www.hackerrank.com/challenges/interviews/problem
Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are 0.
*/
select C.contest_id, C.hacker_id, C.name,
sum(total_submissions) as total_submissions,
sum(total_accepted_submissions) as total_accepted_submissions,
sum(total_views) as total_views,
sum(total_unique_views) as total_unique_views
from Contests C

join Colleges Col on Col.contest_id = C.contest_id
join Challenges Cha on Col.college_id = Cha.college_id

left join
(select challenge_id,
sum(total_views) as total_views,
sum(total_unique_views) as total_unique_views from
View_Stats
group by challenge_id) vs
on Cha.challenge_id = vs.challenge_id

left join
(select challenge_id,
sum(total_submissions) as total_submissions,
sum(total_accepted_submissions) as total_accepted_submissions from
Submission_Stats
group by challenge_id) ss
on Cha.challenge_id = ss.challenge_id

group by C.contest_id, C.hacker_id, C.name
having total_submissions > 0 or
    total_accepted_submissions > 0 or
    total_views > 0 or
    total_unique_views > 0

order by C.contest_id
