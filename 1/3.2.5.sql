SELECT *
FROM sc AS a
WHERE `C#` = 'EE-01'
    AND Grade = (
        SELECT MAX(Grade)
        from sc AS b
        WHERE a.`C#` = b.`C#`
    )