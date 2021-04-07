UPDATE course
SET Period = 56,
    Credit = Credit + 1
WHERE Teacher = '张明'
    AND Cname = '信号与系统'