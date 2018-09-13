SELECT name, weight, price, CAST(ROUND(CAST(price / weight * 1000 AS NUMERIC), 2) AS FLOAT)as price_per_kg
FROM products
ORDER BY price_per_kg ASC, name ASC;