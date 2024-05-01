import sqlite3

conn = sqlite3.connect('architecture.db')

cur = conn.cursor()

cur.execute(''' SELECT * FROM Buildings
                ''')

buildings = cur.fetchall()

for building in buildings:
    print(building)