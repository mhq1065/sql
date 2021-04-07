SELECT Sname,
    AVG(grade) as a
FROM sc
    JOIN student USING (`S#`)
GROUP BY `S#`
HAVING a > 80