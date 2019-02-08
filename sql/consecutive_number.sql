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

-- consecutive available seats https://leetcode.com/problems/consecutive-available-seats/
select distinct c1.seat_id
from cinema c1,
cinema c2
where c1.free = 1 and c2.free = 1
# two consecutive seat
and abs(c1.seat_id - c2.seat_id) = 1
order by seat_id;

/*
write a query to display the records which have 3 or more consecutive rows
and the amount of people more than 100(inclusive)

Human Traffic of Stadium
https://leetcode.com/problems/human-traffic-of-stadium/
*/
select distinct s1.*
from
stadium s1,
stadium s2,
stadium s3
where
s1.people >= 100 and s2.people >=100 and s3.people >= 100
and (
    (s1.id - s2.id = 1 and s1.id - s3.id = 2) or
    (s2.id - s1.id = 1 and s2.id - s3.id = 2) or
    (s3.id - s2.id = 1 and s3.id - s1.id = 2)
)
order by s1.id
