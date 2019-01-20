/*
https://www.hackerrank.com/challenges/what-type-of-triangle/problem

Equilateral: It's a triangle with 3 sides of equal length.
Isosceles: It's a triangle with 2 sides of equal length.
Scalene: It's a triangle with 3 sides of differing lengths.
Not A Triangle:
*/

select
case when A + B <= C or A + C <= B or B + C <= A then 'Not A Triangle'
    when A = B and B = C then 'Equilateral'
    when A = B or B = C or A = C then 'Isosceles'
    else 'Scalene' end
from TRIANGLES
