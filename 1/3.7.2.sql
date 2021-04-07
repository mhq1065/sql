CREATE VIEW `赵明course` AS
SELECT `C#`,
    Cname,
    AVG(Grade)
FROM course
    LEFT JOIN sc USING(`C#`)
WHERE Teacher = '张明'
GROUP BY `C#`