SELECT `S#`,
    SUM(credit)
FROM sc
    JOIN course USING (`C#`)
GROUP BY `S#`
HAVING COUNT(*) >= 3
ORDER BY `S#` ASC