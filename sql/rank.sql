CREATE TABLE t (
    val INT
);

INSERT INTO t(val)
VALUES(1),(2),(2),(3),(4),(4),(5);


SELECT
    *
FROM
    t;

/*
Assigns a rank to every row within its partition based on the ORDER BY clause.
It assigns the same rank to the rows with equal values.
If two or more rows have the same rank, then there will be no gaps in the sequence of ranked values.
*/

-- dense_rank
SELECT
    val,
    DENSE_RANK() OVER (
        ORDER BY val
    ) my_rank
FROM
    t;
