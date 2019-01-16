/*
difference between WITH and VIEW
https://stackoverflow.com/questions/10674761/difference-between-sql-view-and-with-clause

music_action columns:
actionID, clientID, musicID, snapshotDay

summary_table each row is the number of times each clientID
listened to musicID up to endDate. columns:
clientID, numPlay, musicID, endDate
*/

/*
update the summary_table using the music_action table with the latest snapshotDay
注意 summary_table 可能包含有 music_action  没有的信息 所以要 outer join
*/
with new_summary as (
select clientid, musicid,
  count(actionid) as cnt,
  max(snapshotday) as enddate
  from music_action
  group by clientid, musicid
)

select new.clientid,
(new.cnt + old.numplay) as numplay,
new.musicid,
case
  when (old.enddate is null or old.enddate < new.enddate) then new.enddate
  else old.enddate
  end as enddate
from new_summary new
left outer join summary_table old
on old.clientid = new.clientid and
old.musicid = new.musicid
