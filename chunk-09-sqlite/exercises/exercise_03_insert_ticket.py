import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

#creating a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets(
    ticket_id TEXT,
    customer TEXT,
    used INTEGER
)
""")

connection.commit()

#adding a new ticket
cursor.execute(
    "INSERT INTO tickets(ticket_id, customer, used) VALUES (?, ?, ?)",
    ("abcd", "adelina", 0)
)

#commiting the changes
connection.commit()

#confirm the new changes
print("Ticket added")

#close the connection
connection.close()