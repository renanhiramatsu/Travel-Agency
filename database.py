import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hotels (hotel_id INTEGER PRIMARY KEY, name TEXT, city TEXT, stars REAL, price REAL)"

cursor.execute(create_table)
connection.commit()
connection.close()
