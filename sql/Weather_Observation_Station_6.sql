-- start with
select distinct CITY from STATION
where lower(CITY) regexp '^[aeiou]'

-- end with
select distinct CITY from STATION
where lower(CITY) regexp '[aeiou]$'

-- start with and end with
-- . matches any character except a newline.
-- * Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible
select distinct CITY from STATION
where lower(CITY) regexp '^[aeiou].*[aeiou]$'

-- not start and not end with vowels
-- ^ inside of [] means not match, [^5] will match any character except '5'
select distinct city
from station
where lower(city) regexp '^[^aeiou].*[^aeiou]$'

-- not start with vowels or not end with vowels
select distinct city
from station
where lower(city) regexp '^[^aeiou]' OR lower(city) regexp '[^aeiou]$'
