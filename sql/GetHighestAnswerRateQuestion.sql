/*
https://leetcode.com/problems/get-highest-answer-rate-question/
*/
-- number of answers
-- number of shows

select question_id as survey_log
from (
    select question_id,
    sum(case when action = 'answer' then 1 else 0 end) as answers,
    sum(case when action = 'show' then 1 else 0 end) as shows
    from survey_log
    group by question_id
) s
order by answers/shows desc
limit 1
