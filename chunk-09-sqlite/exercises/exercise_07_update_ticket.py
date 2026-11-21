import sqlite3

#connect to tickets.db
connection = sqlite3.connect("tickets.db")

#create cursor
cursor = connection.cursor()

#ask for ticket
active_ticket = input("Enter ticket number: ").strip().lower()

#search for the tickets
cursor.execute(
    "SELECT * FROM tickets WHERE ticket_id = ?",
    (active_ticket,)
)

ticket = cursor.fetchone()

if ticket is None:
    print("Ticket not found")
elif ticket[2] == 1:
    print("Ticket already used")
else:
    cursor.execute(
        "UPDATE tickets SET used = ? WHERE ticket_id = ?",
        (1, active_ticket)
    )
    print("ticket marked as used")

#commit new changes
connection.commit()

#close connection
connection.close()