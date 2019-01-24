CREATE TABLE scores (
    name VARCHAR(20) PRIMARY KEY,
    score INT NOT NULL
);

INSERT INTO
 scores(name, score)
VALUES
 ('Smith',81),
 ('Jones',55),
 ('Williams',55),
 ('Taylor',62),
 ('Brown',62),
 ('Davies',84),
 ('Evans',87),
 ('Wilson',72),
 ('Thomas',72),
 ('Johnson',100);

 /*
Calculates the cumulative distribution of a value in a set of values.
CUME_DIST() = ROW_NUMBER() / total_rows
 */

SELECT
 name,
    score,
    ROW_NUMBER() OVER (ORDER BY score) row_num,
    CUME_DIST() OVER (ORDER BY score) cume_dist_val
FROM
 scores;
