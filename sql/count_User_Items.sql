/*
Let’s assume that we have a database that consists of three tables.

Users
Items
User_Items

*/
create view User_Items_Extended as (
  select
    User_Items.Cust_Names,
    case when Item_Type = "Computer" then Item_Amount end as Computer,
    case when Item_Type = "Monitor" then Item_Amount end as Monitor,
    case when Item_Type = "Software" then Item_Amount end as Software
  from User_Items
);

create view User_Items_Extended_Pivot as (
  select
    Cust_Names,
    sum(Computer) as Computer,
    sum(Monitor) as Monitor,
    sum(Software) as Software
  from User_Items_Extended
  group by Cust_Names
);

create view User_Items_Extended_Pivot_Pretty as (
  select
    Cust_Names,
    coalesce(Computer, 0) as Computer,
    coalesce(Monitor, 0) as Monitor,
    coalesce(Software, 0) as Software
  from User_Items_Extended_Pivot
);
