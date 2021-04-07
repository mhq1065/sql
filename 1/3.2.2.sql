-- 2
SELECT Sname
FROM Student,
    sc
WHERE Student.`S#` = sc.`S#`
    AND Student.sex = '女'
    AND sc.`C#` = 'EE-01';
