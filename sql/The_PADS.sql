/*
1. Query an alphabetically ordered list of all names in OCCUPATIONS,
immediately followed by the first letter of each profession as a parenthetical
(i.e.: enclosed in parentheses). For example: AnActorName(A),
ADoctorName(D), AProfessorName(P), and ASingerName(S).

2. Query the number of ocurrences of each occupation in OCCUPATIONS.
Sort the occurrences in ascending order, and output them in the following format:
There are a total of [occupation_count] [occupation]s.
*/
select concat(Name, '(', left(Occupation, 1), ')')
from OCCUPATIONS
order by Name;

select concat('There are a total of ', count(*), ' ', lower(Occupation), 's.')
from OCCUPATIONS
group by Occupation
order by count(*), Occupation;
