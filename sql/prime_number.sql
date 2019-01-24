/*
Write a query to print all prime numbers less than or equal to .
Print your result on a single line, and use the ampersand (&) character as
your separator (instead of a space).

why use information_schema.tables twice?
Because information_schema.tables has less than 1000 rows.
so i need to multiply two (or more) tables with more than sqrt(1000)=32 rows
*/
select group_concat(b separator '&')
from (select @num := @num + 1 as b
      from information_schema.tables t1,
      information_schema.tables t2,
      (select @num := 1) tmp1) table1
where b <= 1000 and not exists
(select a from
    (select @nu := @nu + 1 as a
    from information_schema.tables t1,
     information_schema.tables t2,
     (select @nu := 1) tmp2) table2
 where a > 1 and a < b and floor(b/a) = (b/a)
)
