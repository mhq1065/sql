SELECT "S#",
	"C#",
	"GRADE"
FROM "JSC802"
	JOIN "JS802" USING ("S#")
WHERE "SEX" = '女'
	AND "S#" NOT IN (
		SELECT "S#"
		FROM "JSC802"
		WHERE "C#" = 'CS-01'
	)