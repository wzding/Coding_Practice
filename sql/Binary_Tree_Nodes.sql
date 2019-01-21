/*
https://www.hackerrank.com/challenges/binary-search-tree-1/problem

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:
*/

-- 注意如果写 when N not in (select distinct P from BST) then 'Leaf' 是错的！！
select distinct N,
case when P is Null then 'Root'
     when N in (select distinct P from BST) then 'Inner'
     else 'Leaf' end as type
from BST
order by N
