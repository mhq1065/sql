DELETE FROM student
where `S#` IN (
        SELECT `S#`
        FROM sc
            JOIN course USING (`C#`)
        GROUP BY `S#`
        HAVING SUM(credit) > 110
    )