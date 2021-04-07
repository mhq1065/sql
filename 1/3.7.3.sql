CREATE VIEW `人工智能学生` AS
SELECT `S#`,
    Sname,
    Grade
FROM student
    JOIN sc USING (`S#`)
WHERE `C#` in (
        SELECT `C#`
        from course
        WHERE Cname = '人工智能'
    )