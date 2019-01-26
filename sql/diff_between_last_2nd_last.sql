/*
LAG: Returns the value of the Nth row before the current row in a partition.
It returns NULL if no preceding row exists.

LAG(<expression>[,offset[, default_value]]) OVER (
    PARTITION BY expr,...
    ORDER BY expr [ASC|DESC],...
)
LEAD: Returns the value of the Nth row after the current row in a partition.
It returns NULL if no subsequent row exists.

LEAD(<expression>[,offset[, default_value]]) OVER (
    PARTITION BY (expr)
    ORDER BY (expr)
)

For each user_id, find the difference between the last action and the second
last action. Action here is defined as visiting a page. If the user has just
one action, you can either remove her from the final results or keep that
user_id and have NULL as time difference between the two actions.

The table below shows for each user all the pages she visited and the corresponding timestamp.
Column  |   Name  |  Value Description
user_id | 6684 |  this is id of the user
page  |  home_page |  the page visited
unix_timestamp |  1451640067 |  unix timestamp in seconds
*/
CREATE TABLE t1 (
    user_id INT NOT NULL,
    page VARCHAR(10) NOT NULL,
    unix_timestamp INT NOT NULL
);

insert into t1(user_id, page, unix_timestamp)
values (1, "home", 1451640067),
(1, "home", 1451640068),
(2, "home", 1451640028),
(2, "home", 1451640090),
(2, "home", 1451640030),
(3, "home", 1451640090),
(4, "home", 1451640090);
/*
这里 lag(unix_timestamp, 1) over (partition by user_id order by unix_timestamp)
等于 lead(unix_timestamp, 1) over (partition by user_id order by unix_timestamp desc)
*/
select user_id,
  unix_timestamp - previous_time as diff
  from (
  select user_id,
    unix_timestamp,
    lag(unix_timestamp, 1) over (
    partition by user_id order by unix_timestamp) as previous_time,
    row_number() over (
    partition by user_id order by unix_timestamp desc) as row_num
    from t1
    ) temp
  where row_num = 1
  order by user_id
