CREATE TABLE overtime (
    employee_name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    hours INT NOT NULL,
    PRIMARY KEY (employee_name , department)
);
INSERT INTO overtime(employee_name, department, hours)
VALUES('Diane Murphy','Accounting',37),
('Mary Patterson','Accounting',74),
('Jeff Firrelli','Accounting',40),
('William Patterson','Finance',58),
('Gerard Bondur','Finance',47),
('Anthony Bow','Finance',66),
('Leslie Jennings','IT',90),
('Leslie Thompson','IT',88),
('Julie Firrelli','Sales',81),
('Steve Patterson','Sales',29),
('Foon Yue Tseng','Sales',65),
('George Vanauf','Marketing',89),
('Loui Bondur','Marketing',49),
('Gerard Hernandez','Marketing',66),
('Pamela Castillo','SCM',96),
('Larry Bott','SCM',100),
('Barry Jones','SCM',65);

/*
FIRST_VALUE: Returns the value of the specified expression with respect to
the first row in the window frame.

LAST_VALUE: Returns the value of the specified expression with respect to
the last row in the window frame.
*/

-- Using MySQL FIRST_VALUE() function over the whole query result set example
SELECT
    employee_name,
    hours,
    FIRST_VALUE(employee_name) OVER (
        ORDER BY hours
    ) least_over_time
FROM
    overtime;
-- Using MySQL FIRST_VALUE() over the partition example
SELECT
    employee_name,
    department,
    hours,
    FIRST_VALUE(employee_name) OVER (
        PARTITION BY department
        ORDER BY hours
    ) least_over_time
FROM
    overtime;


/*
The default frame specification is as follows:
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

It means that the frame starts at the first row and ends at the current row
of the result set. Therefore, to get the employee who has the highest overtime,
we changed the frame specification to the following:
RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
This indicates that the frame starts at the first row and ends at the last row of the result set.
*/
-- MySQL LAST_VALUE() over the whole query result example
SELECT
    employee_name,
    hours,
    LAST_VALUE(employee_name) OVER (
        ORDER BY hours
        RANGE BETWEEN
            UNBOUNDED PRECEDING AND
            UNBOUNDED FOLLOWING
    ) highest_overtime_employee
FROM
    overtime;
-- MySQL LAST_VALUE() over the partition example
SELECT
    employee_name,
    department,
    hours,
    LAST_VALUE(employee_name) OVER (
 PARTITION BY department
        ORDER BY hours
        RANGE BETWEEN
     UNBOUNDED PRECEDING AND
            UNBOUNDED FOLLOWING
 ) most_overtime_employee
FROM
    overtime;
