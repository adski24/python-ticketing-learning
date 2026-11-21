import uuid
import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

while True:
    # create a ticket id
    ticket_id = str(uuid.uuid4())[:8]

    # check to see if it exists
    cursor.execute(
        "SELECT * FROM tickets WHERE ticket_id = ?",
        (ticket_id,)
    )

    existing_ticket = cursor.fetchone()

    if existing_ticket is None:
        break

name = input("What is the name on the ticket? ").strip().lower()

cursor.execute(
    "INSERT INTO tickets VALUES (?, ?, ?)",
    (ticket_id, name, 0)
)

connection.commit()

print("Ticket created:", ticket_id)

connection.close()
