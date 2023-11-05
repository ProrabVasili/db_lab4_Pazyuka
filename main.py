import psycopg2
import matplotlib.pyplot as plt

username = ''
password = ''
database = ''
host = ''
port = ''

query_1 = '''
SELECT city, ROUND(AVG(rating) :: NUMERIC, 2) AS avg_rating
FROM restaurant
JOIN location USING (city_id)
GROUP BY city
'''

query_2 = '''
SELECT type_cuisine, COUNT(*)
FROM restaurant
JOIN restaurant_cuisine USING(restaurant_id)
JOIN cuisine USING (cuisine_id)
GROUP BY type_cuisine;
'''

query_3 = '''
SELECT city, COUNT(DISTINCT cuisine_id)
FROM restaurant
JOIN restaurant_cuisine USING(restaurant_id)
JOIN location USING(city_id)
GROUP BY city
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    cur.execute(query_1)
    
    print('Average rating of restaurants by city: ')
    for row in cur:
        print(f'City: {row[0]}, average rating: {row[1]}')

    cur.execute(query_2)
    
    print('\nNumber of restaurants with each type of cuisine: ')
    for row in cur:
        print(f'Type of cuisine: {row[0]}, num of restaurants: {row[1]}')

    cur.execute(query_3)
    
    print('\nNumber of unique cuisine types by city: ')
    for row in cur:
        print(f'City: {row[0]}, num of unique cuisine types: {row[1]}')
    


