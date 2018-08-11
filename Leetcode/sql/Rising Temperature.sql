SELECT w1.Id AS "Id"
FROM weather w1, weather w2
WHERE w1.RecordDate - 1 = w2.RecordDate AND
    w1.Temperature > w2.Temperature;