SELECT class
FROM(
    SELECT class, COUNT(DISTINCT student) AS cnt
    FROM courses
    GROUP BY class
    ) AS counts
WHERE cnt >= 5;