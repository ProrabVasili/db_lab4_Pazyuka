-- Find restaurants with rating between 3.5 and 4.5
SELECT restaurant_name
FROM restaurant
WHERE rating BETWEEN 3.5 AND 4.5;

-- Find restaurants with Bakery cuisine
SELECT restaurant_name
FROM restaurant
JOIN restaurant_cuisine USING (restaurant_id)
WHERE cuisine_id = (SELECT cuisine_id
				   FROM cuisine
				   WHERE type_cuisine = 'Bakery');
				   
-- Calucalate average rating of restaurants by city (name as avg_rating). 
-- Sort avg_rating descending
SELECT city, ROUND(AVG(rating) :: NUMERIC, 2) AS avg_rating
FROM restaurant
JOIN location USING (city_id)
GROUP BY city
ORDER BY avg_rating DESC;