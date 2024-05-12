import sqlite3


connection = sqlite3.connect("test.sqlite3")
cursor = connection.cursor()

cursor.execute('SELECT * FROM User')

variable = cursor.fetchall()


connection.close()

print(variable)  # [(1, 'admin'), (2, 'user')]