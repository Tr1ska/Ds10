import sqlite3

connection = sqlite3.connect("Ds10_DB.sl3", 5)

cur = connection.cursor()

cur.execute("INSERT INTO dz_3 (name, temperature) VALUES ('Lviv', '23');")

connection.commit()

