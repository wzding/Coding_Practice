/* create 3 tables:
accounts
dates
facts
find a list of all accounts on every day in the last 3 days that
had no expense
 */

create table accounts(
  accountid int
);

insert into accounts (accountid) values
  (1),
  (2),
  (3);

create table dates(
  dateid DATE
);

insert into dates (dateid) values
  ('2018-01-01'), ('2018-01-02'), ('2018-01-03'), ('2018-01-03'),
  ('2018-01-04'), ('2018-01-05'), ('2018-01-06'), ('2018-01-07'),
  ('2018-01-08'), ('2018-01-09'), ('2018-01-10'), ('2018-01-11'),
  ('2018-01-12'), ('2018-01-13'), ('2018-01-14'), ('2018-01-15');

create table facts(
  accountid int,
  dateid DATE,
  revenue NUMERIC
);

insert into facts (accountid, dateid, revenue) values
  (1, '2018-01-01', 3), (2, '2018-01-02', 5), (3, '2018-01-03', 6),
  (1, '2018-01-04', 7), (1, '2018-01-05', 4), (1, '2018-01-06', 5),
  (1, '2018-01-08', 4), (2, '2018-01-09', 1), (3, '2018-01-10', 4),
  (1, '2018-01-12', 5), (2, '2018-01-13', 1), (2, '2018-01-14', 1);


select d.dateid, a.accountid
from dates d
cross join accounts a
-- have expense
left join (
  select distinct facts.accountid, dates.dateid as dateid
  from facts cross join dates
  where dates.dateid >= facts.dateid
  and dates.dateid <= facts.dateid + 3
) active on
active.dateid = d.dateid and
active.accountid = a.accountid
where active.dateid is NULL

-- +------------+-----------+
-- | dateid     | accountid |
-- +------------+-----------+
-- | 2018-01-01 |         2 |
-- | 2018-01-01 |         3 |
-- | 2018-01-02 |         3 |
-- | 2018-01-06 |         2 |
-- | 2018-01-07 |         2 |
-- | 2018-01-07 |         3 |
-- | 2018-01-08 |         2 |
-- | 2018-01-08 |         3 |
-- | 2018-01-09 |         3 |
-- | 2018-01-14 |         3 |
-- | 2018-01-15 |         3 |
-- +------------+-----------+
