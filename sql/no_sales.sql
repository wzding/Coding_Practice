/* create 3 tables:
accounts
dates
facts */

create table accounts(
  accountid int
);

-- insert into accounts (accountid) values
--   (1),
--   (2);

create table dates(
  dateid DATE
);

create table facts(
  accountid int,
  dateid DATE,
  revenue NUMERIC
);

/*
a list of all accounts on every day in the last 30 days that
had no expense
*/
SELECT d.dateid, a.accountid from accounts a
cross join dates d
-- active accounts, note need to select distinct
left outer join (
  select distinct f.accountid, dd.dateid as dateid
  from facts f cross join dates dd
  where (dd.dateid - f.dateid) <= 30
  and (dd.dateid - f.dateid) >= 0
) active on
a.accountid = active.accountid and
d.dateid = active.dateid
where active.dateid is NULL
