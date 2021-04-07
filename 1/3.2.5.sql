SELECT `S#`
FROM sc
WHERE Grade is not Null
    AND `C#` =(
        SELECT `C#`
        FROM course
        WHERE Cname = 'CS-01'
        LIMIT 1
    )
ORDER BY Grade DESC
limit 1