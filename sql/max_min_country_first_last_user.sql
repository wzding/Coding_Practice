CREATE TABLE country_table (
    user_id INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    country VARCHAR(10) NOT NULL
);

INSERT INTO country_table(user_id, created_at, country)
VALUES (1,'2014-03-30', 'China'),
(2,'2014-01-30', 'US'),
(5,'2014-01-10', 'US'),
(6,'2014-01-20', 'US'),
(3,'2014-02-10', 'Japan'),
(7,'2014-01-10', 'Japan'),
(4,'2014-05-30', 'US');

-- The country with the largest and smallest number of users
SELECT
(
  SELECT country FROM country_table
  group by country
  having COUNT(user_id) = (
    select max(cnt) from
    (select count(user_id) as cnt from country_table group by country
    ) max_count
  )
) as max_country,
(
  SELECT country FROM country_table
  group by country
  having COUNT(user_id) = (
    select min(cnt) from
    (select count(user_id) as cnt from country_table group by country
    ) min_count
  )
) as min_country;
-- +-------------+-------------+
-- | max_country | min_country |
-- +-------------+-------------+
-- | US          | China       |
-- +-------------+-------------+
-- 下面的方法也是输出用户最多和最少的国家 但是输出结果有点不同
select country, s from
(
  select country, s,
  row_number() over(order by s) as row_a,
  row_number() over(order by s desc) as row_b
  from (
    select country,
    count(distinct user_id) as s
    from country_table
    group by country) cnt_table) tmp
  where row_a = 1 or row_b = 1;
-- +---------+---+
-- | country | s |
-- +---------+---+
-- | US      | 4 |
-- | China   | 1 |
-- +---------+---+
/* A query that returns for each country the first and the last user who
signed up (if that country has just one user, it should just return that single user)
*/
select country,
(
  select user_id from country_table
  where country = t.country and
  created_at = (select min(created_at) from country_table
  where country = t.country)
) first_user,
(
  select user_id from country_table
  where country = t.country and
  created_at = (select max(created_at) from country_table
  where country = t.country)
) last_user
from country_table t
group by country
-- +---------+------------+-----------+
-- | country | first_user | last_user |
-- +---------+------------+-----------+
-- | China   |          1 |         1 |
-- | US      |          5 |         4 |
-- | Japan   |          7 |         3 |
-- +---------+------------+-----------+
-- 下面的方法也是输出最早最晚注册的用户 但是输出结果有点不同
select user_id, created_at, country
from
(
  select *,
  row_number() over(partition by country order by created_at) as row_a,
  row_number() over(partition by country order by created_at desc) as row_b
  from country_table
) tmp
  where row_a = 1 or row_b = 1;
-- +---------+---------------------+---------+
-- | user_id | created_at          | country |
-- +---------+---------------------+---------+
-- |       1 | 2014-03-30 00:00:00 | China   |
-- |       3 | 2014-02-10 00:00:00 | Japan   |
-- |       7 | 2014-01-10 00:00:00 | Japan   |
-- |       4 | 2014-05-30 00:00:00 | US      |
-- |       5 | 2014-01-10 00:00:00 | US      |
-- +---------+---------------------+---------+
