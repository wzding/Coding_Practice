/*
这题很tricky
https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem

total number of unique hackers who made at least 1 submission each day
find the hacker_id and name of the hacker who made maximum number of submissions each day.
If more than one such hacker has a maximum number of submissions, print the lowest hacker_id.

The query should print this information for each day of the contest, sorted by the date.
*/
SELECT
    submission_date,
(SELECT
 COUNT(distinct hacker_id)
 FROM Submissions s1
 WHERE s1.submission_date = dates.submission_date
 -- made at least  submission each day
 AND (SELECT
      COUNT(distinct s2.submission_date)
      FROM Submissions s2
      WHERE s2.hacker_id = s1.hacker_id
      AND s2.submission_date < dates.submission_date)
                = datediff(dates.submission_date , '2016-03-01')
     ) ,
-- made maximum number of submissions each day
(SELECT
    hacker_id
    FROM submissions s3
    WHERE s3.submission_date = dates.submission_date
    GROUP BY hacker_id
    ORDER BY count(submission_id) DESC , hacker_id limit 1) as topHack,
(SELECT
    name
    FROM hackers
    WHERE hacker_id = topHack)

  FROM (SELECT distinct submission_date from submissions) dates
