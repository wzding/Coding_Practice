/*
difference between WITH and VIEW
https://stackoverflow.com/questions/10674761/difference-between-sql-view-and-with-clause

music_action columns:
actionID, clientID, musicID, snapshotDay

summary_table each row is the number of times each clientID
listened to musicID up to endDate. columns:
clientID, numPlay, musicID, endDate
*/
create table music_table (
  actionid int,
  clientid int,
  musicid int,
  snapshotday timestamp
);
insert into music_table (actionid, clientid, musicid, snapshotday) values
(1, 1, 1, '20180101'),
(2, 2, 1, '20180201'),
(3, 1, 7, '20180301'),
(4, 1, 1, '20180402'),
(5, 3, 1, '20180501'),
(6, 2, 1, '20180601'),
(7, 1, 3, '20180701'),
(8, 4, 4, '20180801');

create table summary_table (
  clientid int,
  numplay int,
  musicid int,
  enddate timestamp
);
insert into summary_table (clientid, numplay, musicid, enddate) values
(1, 3, 1, '20180401'),
(2, 4, 2, '20180201');

/*
update the summary_table using the music_action table with the latest snapshotDay
music_action 是全集 summary_table 是子集
注意 music_action 可能包含有 summary_table 没有的信息 所以要 outer join
*/
select n.clientid,
case
  when s.numplay is not null then s.numplay + n.numplay
  else n.numplay end as numplay,
n.musicid,
case
  when s.enddate is null or s.enddate < n.enddate then n.enddate
  else s.enddate end as enddata
from
  (select clientid, musicid,
  count(actionid) as numplay,
  max(snapshotday) as enddate
  from music_table
  group by clientid, musicid) n
left join summary_table s
on s.clientid = n.clientid and s.musicid = n.musicid
order by n.clientid, n.enddate
-- +----------+---------+---------+---------------------+
-- | clientid | numplay | musicid | enddata             |
-- +----------+---------+---------+---------------------+
-- |        1 |       1 |       7 | 2018-03-01 00:00:00 |
-- |        1 |       5 |       1 | 2018-04-02 00:00:00 |
-- |        1 |       1 |       3 | 2018-07-01 00:00:00 |
-- |        2 |       2 |       1 | 2018-06-01 00:00:00 |
-- |        3 |       1 |       1 | 2018-05-01 00:00:00 |
-- |        4 |       1 |       4 | 2018-08-01 00:00:00 |
-- +----------+---------+---------+---------------------+
