import uuid
import sqlite3

#connect to tickets.db
connection = sqlite3.connect("tickets.db")

#create a cursor
cursor = connection.cursor()

#generating a short ticket id
ticket_id = str(uuid.uuid4())[:8]

#ask for customer name
name = input("Please enter your name: ").strip().lower()

#inserting ticket into the system
cursor.execute(
    "INSERT INTO tickets (ticket_id, customer, used) VALUES (?, ?, ?)",
    (ticket_id, name, 0)
)
connection.commit()
print(ticket_id)
connection.close()