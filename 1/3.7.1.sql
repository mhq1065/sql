CREATE VIEW `View1` AS
SELECT `S#`,
    Sname,
    Bdate,
    Height
FROM student
WHERE Dorm = '西18'
    AND Sex = '男';