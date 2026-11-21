import sqlite3

#create connection to tickets
connection = sqlite3.connect("tickets.db")

#create cursor
cursor = connection.cursor()

#asking for ticket input
active_ticket = input("Enter ticket number: ").strip().lower()

#search the list for specific id
cursor.execute(
    "SELECT * FROM tickets WHERE ticket_id = ?",
    (active_ticket,)
)

#return the found ticket
ticket = cursor.fetchone()

if ticket is None:
    print("Ticket not found")
else:
    print(ticket)

#close the connection
connection.close()