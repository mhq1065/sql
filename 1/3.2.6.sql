SELECT Sname,
    course.`C#`,
    course.Credit,
    sc.Grade
FROM sc
    JOIN student USING (`S#`)
    JOIN course USING (`C#`)