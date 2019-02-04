/*
 find the overall acceptance rate of requests rounded to 2 decimals,
 which is the number of acceptance divide the number of requests.
How about the cumulative accept rate for every day?
*/
CREATE TABLE friend_request (
    sender_id INT NOT NULL,
    send_to_id INT NOT NULL,
    request_date DATE NOT NULL
);
INSERT INTO friend_request(sender_id, send_to_id, request_date)
VALUES (1, 2, '2016-06-01'),
(1, 3, '2016-06-01'),
(1, 4, '2016-06-01'),
(2, 3, '2016-06-02'),
(3, 4, '2016-06-09');

CREATE TABLE request_accepted (
    requester_id INT NOT NULL,
    accepter_id INT NOT NULL,
    accept_date DATE NOT NULL
);
INSERT INTO request_accepted(requester_id, accepter_id, accept_date)
VALUES (1, 2, '2016-06-03'),
(1, 3, '2016-06-08'),
(2, 3, '2016-06-08'),
(3, 4, '2016-06-09'),
(3, 4, '2016-06-10');

select day,
round(acp_cum_sum / req_cum_sum, 2) as accept_rate
from
-- cum sum
(
  select day,
  sum(req_num) over (order by day) as req_cum_sum,
  sum(acp_num) over (order by day) as acp_cum_sum
  from
  -- fill nan
  (
      select day,
      case when req_num is null then 0 else req_num end as req_num,
      case when acp_num is null then 0 else acp_num end as acp_num
      from
      -- all days
      (
          (select distinct request_date as day from friend_request)
          union
          (select distinct accept_date as day from request_accepted)
      ) all_date
      -- join request
      left join
      (
          select request_date,
          count(distinct sender_id, send_to_id) as req_num
          from (
            select sender_id, send_to_id, min(request_date) as request_date
            from friend_request
            group by sender_id, send_to_id
          ) f
          group by request_date
      ) req
      on all_date.day = req.request_date
      -- join acceptance
      left join
      (
          select accept_date,
          count(distinct requester_id, accepter_id) as acp_num
          from (
            select requester_id, accepter_id, min(accept_date) as accept_date
            from request_accepted
            group by requester_id, accepter_id
          ) r
          group by accept_date
      ) acp
      on all_date.day = acp.accept_date
      order by day
  ) fill_nan_table
) cum_table
