import sqlite3
import uuid

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

while True:
    ticket_id = str(uuid.uuid4())[:8]

    #search for the id
    cursor.execute(
        "SELECT * FROM tickets WHERE ticket_id = ?",
        (ticket_id,)
    )
    existing_ticket = cursor.fetchone()

    if existing_ticket is None:
        break

name = input("Enter your name: ").strip().lower()
cursor.execute(
    "INSERT INTO tickets VALUES (?, ?, ?)",
    (ticket_id, name, 0)
    )

connection.commit()
connection.close()
print("Ticket created:", ticket_id)
