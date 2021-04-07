-- 3
SELECT Sname
FROM Student
WHERE `S#` IN (
        SELECT DISTINCT `S#`
        FROM SC
        WHERE `S#` <> 'CS-01'
    );
