/*
https://leetcode.com/problems/delete-duplicate-emails/
delete all duplicate email entries in a table named Person,
keeping only unique emails based on its smallest Id.
*/
delete p1
from
    Person p1
    join Person p2
    on p1.Email = p2.Email and p1.id > p2.id
