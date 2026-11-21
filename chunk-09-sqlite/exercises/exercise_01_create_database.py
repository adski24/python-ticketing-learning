import sqlite3

connection = sqlite3.connect('tickets.db')
print("Database connected")
connection.close()
print("Database closed")