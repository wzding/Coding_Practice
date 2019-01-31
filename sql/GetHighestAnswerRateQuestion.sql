/*
https://leetcode.com/problems/get-highest-answer-rate-question/
*/
-- number of answers
-- number of shows

select question_id as survey_log
from (
    select
    question_id,
    sum(case action when 'answer' then 1 else 0 end
    ) / sum(
      case action when 'show' then 1 else 0 end) as ratio
    from survey_log
    group by question_id
) tmp
order by ratio desc
limit 1
