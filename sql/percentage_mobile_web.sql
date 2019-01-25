/*
One table has all mobile actions, i.e. all pages visited by the users on mobile.
The other table has all web actions, i.e. all pages visited on web by the users.
Write a query that returns the percentage of users who only visited mobile,
only web and both. That is, the percentage of users who are only in the mobile
table, only in the web table and in both tables. The sum of the percentages should return 1.
*/

CREATE TABLE t1 (
    user_id INT NOT NULL,
    page VARCHAR(10) NOT NULL
);
CREATE TABLE t2 (
    user_id INT NOT NULL,
    page VARCHAR(10) NOT NULL
);

insert into t1(user_id, page, unix_timestamp)
values (1, "m"),
(2, "m"),
(3, "m"),
(4, "m"),
(5, "m"),
(6, "m"),
(7, "m");

insert into t2(user_id, page, unix_timestamp)
values (3, "w"),
(5, "w"),
(7, "w"),
(9, "w"),
(10, "w"),
(11, "w"),
(12, "w");

-- my sql does not have full outer join, use union all instead
-- 如果t1 或者 t2有重复 把 SELECT t1.page as page 变成 SELECT distinct t1.page as page

select
sum(
  case when page = 'm' and both_user is Null
  then 1 else 0 end) / count(distinct user_id)
  as m_only,
sum(
  case when page = 'w' and  both_user is Null
  then 1 else 0 end) / count(distinct user_id)
  as w_only,
sum(
  case when page = 'm' and both_user is not Null
  then 1 else 0 end) / count(distinct user_id)
  as m_w
from (
  (SELECT t1.page as page,
   t1.user_id as user_id,
   t2.user_id as both_user
   FROM t1
  left join t2 on t1.user_id = t2.user_id)
  Union  all
  (SELECT t2.page as page,
   t2.user_id as user_id,
   t1.user_id as both_user
   FROM t2
  left join t1 on t2.user_id = t1.user_id)
) all_data
