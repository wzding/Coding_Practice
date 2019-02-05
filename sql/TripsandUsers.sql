/*
https://leetcode.com/problems/trips-and-users/
find the cancellation rate of requests made by unbanned users between Oct 1,
2013 and Oct 3, 2013. For the above tables,
*/

select Request_at as Day,
round(cancelations / total_trips, 2) as 'Cancellation Rate'
from
(
    select
    Request_at,
    sum(case when Status != 'completed' then 1 else 0 end) as cancelations,
    count(*) as total_trips
    from (
        select
        Request_at,
        Status,
        u1.Banned as client_banned,
        u2.Banned as driver_banned
        from Trips t
        left join Users u1
        on t.Client_Id = u1.Users_id
        left join Users u2
        on t.Driver_Id = u2.Users_id
    ) tmp1
    where client_banned = "No" and driver_banned = "No"
    and Request_at between '2013-10-01' and '2013-10-03'
    group by Request_at
) tmp2

-- +------------+-------------------+
-- |     Day    | Cancellation Rate |
-- +------------+-------------------+
-- | 2013-10-01 |       0.33        |
-- | 2013-10-02 |       0.00        |
-- | 2013-10-03 |       0.50        |
-- +------------+-------------------+
