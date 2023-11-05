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
ORDER BY avg_rating DESC;
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
GROUP BY city;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    figure, (bar1_ax, pie_ax, bar2_ax) = plt.subplots(1, 3)
    cur = conn.cursor()

    cur.execute(query_1)

    cities = []
    ratings = []
    for row in cur:
        cities.append(row[0])
        ratings.append(float(row[1]))
        
    x_range = range(len(cities))
 
    bar1_ax.bar(x_range, ratings)
    bar1_ax.set_title('Average rating of restaurants by city')
    bar1_ax.set_xlabel('Cities')
    bar1_ax.set_ylabel('Average rating')
    bar1_ax.set_xticks(x_range)
    bar1_ax.set_xticklabels(cities, rotation=45)
    bar1_ax.set_yticks([i/2 for i in range(int(max(ratings)+1)*2)])
    
    cur.execute(query_2)

    cuisines = []
    nums = []
    for row in cur:
        cuisines.append(row[0])
        nums.append(int(row[1]))
        
    pie_ax.pie(nums, labels=cuisines, autopct='%1.2f%%')
    pie_ax.set_title('Share of each type of cuisine')

    cur.execute(query_3)

    cities = []
    nums = []
    for row in cur:
        cities.append(row[0])
        nums.append(int(row[1]))
        
    x_range = range(len(cities))
 
    bar2_ax.bar(x_range, nums)
    bar2_ax.set_title('Number of unique cuisine types by city')
    bar2_ax.set_xlabel('Cities')
    bar2_ax.set_ylabel('Num of unique cuisine types')
    bar2_ax.set_xticks(x_range)
    bar2_ax.set_yticks(range(max(nums)+2))
    bar2_ax.set_xticklabels(cities, rotation=45)
     


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()

