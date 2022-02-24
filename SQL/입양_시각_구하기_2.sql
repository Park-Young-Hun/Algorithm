WITH RECURSIVE AH AS (SELECT 0 AS HOUR
                   UNION ALL
                   SELECT HOUR+1
                   FROM AH
                   WHERE HOUR < 23)
SELECT AH.HOUR, COUNT(HOUR(AO.DATETIME)) AS COUNT
FROM AH
LEFT JOIN ANIMAL_OUTS AS AO
ON AH.HOUR = HOUR(AO.DATETIME)
GROUP BY AH.HOUR
ORDER BY AH.HOUR;
