-- 4
SELECT `S#`,Sname,FLOOR(DATEDIFF(CURDATE(), Bdate)/365.2422) 
FROM Student
WHERE Height > (
        SELECT Height
        FROM student
        WHERE Sname = '王涛'
        LIMIT 1
    )