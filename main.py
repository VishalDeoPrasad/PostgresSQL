import psycopg2
conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='admin', port=5432)

cur = conn.cursor()
##################################################
cur.execute("""
            CREATE TABLE IF NOT EXISTS person(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR );""")

# cur.execute("""INSERT INTO person (id, name, age, gender) VALUES  
#     (6, 'John Doe', 30, 'M'),
#     (7, 'Jane Smith', 25, 'F'),
#     (8, 'Michael Johnson', 40, 'M'),
#     (9, 'Emily Davis', 28, 'F'),
#     (10, 'David Brown', 35, 'M'); """)

cur.execute("SELECT * FROM person WHERE name='John Doe';")
print(cur.fetchone())

cur.execute("SELECT * FROM person WHERE gender='M'")
for row in cur.fetchall():
    print(row)
##################################################
conn.commit()
cur.close()
conn.close()