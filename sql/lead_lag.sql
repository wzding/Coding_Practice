/*
https://explainextended.com/2009/03/10/analytic-functions-first_value-last_value-lead-lag/

emulate FIRST_VALUE
SELECT  m.*,
FIRST_ROW(month) OVER (PARTITION BY season ORDER BY id),
LAST_ROW(month) OVER (PARTITION BY season ORDER BY id)
FROM    t_month m

LAG(column) returns the value of column from the previous row in the grouping set,
or NULL if there is no previous row.
LEAD(column) returns the value of column from the next row in the grouping set,
or NULL if there is no next row.
*/
-- emulate FIRST_VALUE
SELECT  *,
@r AS `FIRST_VALUE(month) OVER (PARTITION BY season ORDER BY id)`
FROM (
  SELECT  m.*
  FROM (SELECT @_season = NULL) vars,
  t_month m
  ORDER BY season, id) mo
WHERE (
  CASE WHEN @_season IS NULL OR @_season &lt; &gt; season
  THEN @r := month ELSE month END IS NOT NULL)
  AND (@_season := season) IS NOT NULL

-- emulate LAST_VALUE
SELECT  *,
@r AS `LAST_VALUE(month) OVER (PARTITION BY season ORDER BY id)`
FROM (
  SELECT  m.*
  FROM (SELECT  @_season = NULL) vars, t_month m
  ORDER BY season, id DESC) mo
WHERE (
  CASE WHEN @_season IS NULL OR @_season &lt;&gt; season
  THEN @r := month ELSE month END IS NOT NULL)
  AND (@_season := season) IS NOT NULL

-- LAG
SELECT  mo.id, mo.season,
@r AS `LAG(month) OVER (PARTITION BY season ORDER BY id)`,
(@r := month) AS month
  FROM (SELECT m.*
    FROM (SELECT @_season = NULL, @s := NULL) vars, t_month m
    ORDER BY season, id) mo
WHERE  (
  CASE WHEN @_season IS NULL OR @_season &lt;&gt; season
  THEN @r := NULL ELSE NULL END IS NULL)
  AND (@_season := season) IS NOT NULL

-- LEAD
SELECT  mo.id, mo.season,
@r AS `LEAD(month) OVER (PARTITION BY season ORDER BY id)`,
(@r := month) AS month
  FROM (SELECT m.*
    FROM (SELECT  @_season = NULL, @s := NULL) vars, t_month m
    ORDER BY season, id DESC) mo
WHERE  (
  CASE WHEN @_season IS NULL OR @_season &lt;&gt; season
  THEN @r := NULL ELSE NULL END IS NULL)
  AND (@_season := season) IS NOT NULL
