SELECT *
FROM (SELECT city, LENGTH(city) as len
  FROM station
  ORDER BY len ASC, city ASC)
WHERE ROWNUM <= 1;

SELECT *
FROM (SELECT city, LENGTH(city) as len
  FROM station
  ORDER BY len DESC, city ASC)
WHERE ROWNUM <= 1;
