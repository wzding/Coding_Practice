/*
https://leetcode.com/problems/tree-node/
https://www.hackerrank.com/challenges/binary-search-tree-1/problem

注意如果写 when N not in (select distinct P from BST) then 'Leaf' 是错的！！
原因如下
NOT IN returns 0 records when compared against an unknown value. Since NULL is
an unknown, a NOT IN query containing a NULL or NULLs in the list of possible
values will always return 0 records since there is no way to be sure that the
NULL value is not the value being tested.
*/

select distinct N,
case when P is Null then 'Root'
     when N in (select distinct P from BST) then 'Inner'
     else 'Leaf' end as type
from BST
order by N
