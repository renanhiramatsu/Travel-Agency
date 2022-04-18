import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hotels (hotel_id INTEGER PRIMARY KEY, name TEXT, city TEXT, stars REAL, price REAL)"

create_hotel = "INSERT INTO hotels VALUES (NULL, ?, ?, ?, ?)"


cursor.execute(create_table)
cursor.execute(create_hotel, ('Marriot', 'Cancun', 5, 119.29))

connection.commit()
connection.close()
