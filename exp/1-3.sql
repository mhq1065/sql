SELECT *
FROM "JS802"
WHERE "BDATE" >= to_date('01 Jan 1992', 'DD Mon YYYY')
	AND "BDATE" < to_date('01 Jan 1993', 'DD Mon YYYY')