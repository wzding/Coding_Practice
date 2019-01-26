/*
find all the jobid that appear at least twice consecutively.
*/

create table logs (
  timestamp int,
  jobid int
);

insert into logs (timestamp, jobid) values
(1, 1),
(2, 2),
(3, 1),
(4, 1),
(5, 3),
(6, 2),
(7, 1),
(8, 4);

/* O(n^2) */
select distinct a.jobid
from logs a, logs b
where b.timestamp = a.timestamp + 1
and a.jobid = b.jobid

/* O(n)
can extend to k consecutive dates --> change 2 to k
*/
select distinct jobid
from (select jobid,
      @counter := if(@prev = jobid, @counter := @counter + 1, 1) as cnt,
      @prev := jobid
      from logs,
      (select @counter := 1, @prev := Null) init) counts
where cnt >= 2

/* or set variable first */
set @counter := 1;
set @prev := Null;
select distinct jobid
from (select jobid,
      @counter := if(@prev = jobid, @counter := @counter + 1, 1) as cnt,
      @prev := jobid
     from logs) count
where cnt >= 2;
