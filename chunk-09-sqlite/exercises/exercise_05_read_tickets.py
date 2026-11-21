import sqlite3
#connect to the tickets
connection = sqlite3.connect("tickets.db")

#create a cursor
cursor = connection.cursor()

#select all rows from tickets
cursor.execute("SELECT * FROM tickets")
tickets = cursor.fetchall()

#loop through rows
for ticket in tickets:
    print(ticket)

#close the connection
connection.close()

