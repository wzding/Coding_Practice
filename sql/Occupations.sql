/*
https://www.hackerrank.com/challenges/occupations/problem
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted
alphabetically and displayed underneath its corresponding Occupation.
The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

the following code creates the rows labeled with a row #, and the columns filled in with a Name or NULL value:
set @r1=0, @r2=0, @r3=0, @r4=0;
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name

Output:
RowNumber: Dr_Name: Prof_Name: Singer_Name: Actor_Name:
1 Aamina NULL NULL NULL
1 NULL Ashley NULL NULL
2 NULL Belvet NULL NULL
3 NULL Britney NULL NULL
1 NULL NULL Christeen NULL
1 NULL NULL NULL Eve
2 NULL NULL Jane NULL
2 NULL NULL NULL Jennifer
3 NULL NULL Jenny NULL
2 Julia NULL NULL NULL
3 NULL NULL NULL Ketty
4 NULL NULL Kristeen NULL
4 NULL Maria NULL NULL
5 NULL Meera NULL NULL
6 NULL Naomi NULL NULL
3 Priya NULL NULL NULL
7 NULL Priyanka NULL NULL
4 NULL NULL NULL Samantha

Finally the code aggregates the rows together using the group by
RowNumber and the min statement. As stated below 'min()/max() will return
a name for specific index and specific occupation. If there is a name,
it will return it, if not, return NULL'.

set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
) Temp
group by RowNumber;

Output:
Aamina Ashley Christeen Eve
Julia Belvet Jane Jennifer
Priya Britney Jenny Ketty
NULL Maria Kristeen Samantha
NULL Meera NULL NULL
NULL Naomi NULL NULL
NULL Priyanka NULL NULL
*/

set @r1 := 0, @r2 := 0, @r3 := 0, @r4 := 0;

select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
    select case Occupation
    when 'Doctor' then @r1 := @r1+1
    when 'Professor' then @r2 := @r2+1
    when 'Singer' then @r3 := @r3+1
    when 'Actor' then @r4 := @r4+1
    end as row,
    case Occupation when 'Doctor' then Name end as Doctor,
    case Occupation when 'Professor' then Name end as Professor,
    case Occupation when 'Singer' then Name end as Singer,
    case Occupation when 'Actor' then Name end as Actor
    from OCCUPATIONS
    order by Name
) temp
group by row;

-- use IF rather than case
set @r1 := 0, @r2 := 0, @r3 := 0, @r4 := 0;

select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
    select case Occupation
    when 'Doctor' then @r1 := @r1+1
    when 'Professor' then @r2 := @r2+1
    when 'Singer' then @r3 := @r3+1
    when 'Actor' then @r4 := @r4+1
    end as row,
    If(Occupation = 'Doctor', Name, Null) as Doctor,
    If(Occupation = 'Professor', Name, Null) as Professor,
    If(Occupation = 'Singer', Name, Null) as Singer,
    If(Occupation = 'Actor', Name, Null) as Actor
    from OCCUPATIONS
    order by Name
) temp
group by row;

-- set local variable in table
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
    select case Occupation
    when 'Doctor' then @r1 := @r1+1
    when 'Professor' then @r2 := @r2+1
    when 'Singer' then @r3 := @r3+1
    when 'Actor' then @r4 := @r4+1
    end as row,
    If(Occupation = 'Doctor', Name, Null) as Doctor,
    If(Occupation = 'Professor', Name, Null) as Professor,
    If(Occupation = 'Singer', Name, Null) as Singer,
    If(Occupation = 'Actor', Name, Null) as Actor
    from OCCUPATIONS, (
        select @r1 := 0, @r2 := 0, @r3 := 0, @r4 := 0
    ) init
    order by Name
) temp
group by row;
