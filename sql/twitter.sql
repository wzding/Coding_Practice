/*
1.给了一个table
user_id           action                timestamp
1                    search                  10
1                    like                       13
2                    search                   11
1                    like                        13 + t
如何所有的log分成block，每个block里只能有一个用户，只能有一个search action，
如果两个action的时间差超出了t，就分成两个block.所以上面的output是
(user1, search, like), (user2, search), (user1, like)
*/
create table t (
  id int,
  action varchar(10),
  times int
);

insert into t (id, action, times) values
(1, 'search', 10),
(1, 'like', 13),
(2, 'search', 11),
(1, 'like', 18);

/*
只需要 3 个变量
*/
select id,
group_concat(action separator ', ') as actions
from (
  select *,
  @num := if(id = @prev_id and times - @prev_time <= 4, @num, @num + 1) as num,
  @prev_id := id,
  @prev_time := times
  from t,
  (select @curr := 0, @prev_id := Null, @prev_time := 0) init
  order by id, times
) tmp
group by num, id

/*
2. tweet_id, con_num, reply_to_tweet
1, 1, null  # depth:0
2,1, 1 #depth 1
3,1,2 #depth 2
4,1,1 #depth 1
5,2,null #depth 0
6, 1,3# depth 3

要求 output：depth0，depth1，depth2，depth>=3, count
  depth 0： 2
  depth 1: 2
  depth 2: 1
  depth>=3: 1
*/

create table tweet(
tweet_id int,
Con_num int,
reply_to_tweet int);
insert into tweet values
(1,1,null),(2,1,1),(3,1,2),(4,1,1),(5,2,null),(6,2,5),(7,1,2),(8,1,7);

select depth, count(*) from
(
  select
  case when to_id0 is null then 'depth 0'
       when to_id1 is null then 'depth 1'
       when to_id2 is null then 'depth 2'
       else 'depth 3' end as depth
  from (
    select
    t1.tweet_id,
    t1.Con_num,
    t1.reply_to_tweet as to_id0,
    t2.reply_to_tweet as to_id1,
    t3.reply_to_tweet as to_id2
    from tweet t1
    left join tweet t2
    on t1.reply_to_tweet = t2.tweet_id and t1.Con_num = t2.Con_num
    left join tweet t3
    on t2.reply_to_tweet = t3.tweet_id and t2.Con_num = t3.Con_num
  ) tmp1
) tmp2
group by depth

/*
3.给两个table，一个是abusers的ip address，另一个是所有用户的ip address，算一下有多少abusers回到了平台上
*/
create table abuser (
  id int
);
insert into abuser (id) values
(1),
(2),
(3);
create table user (
  id int
);
insert into user (id) values
(1),
(2),
(3),
(4),
(5);

select count(distinct abuser.id)
from abuser
join user
on abuser.id = user.id
