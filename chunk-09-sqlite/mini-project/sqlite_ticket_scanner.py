import sqlite3

#connect to data
connection = sqlite3.connect('tickets.db')

#create a cursor
cursor = connection.cursor()

#ask for ticket
active_ticket = input("Enter ticket number to scan: ").strip().lower()

#select matching ticket
cursor.execute(
    "SELECT * FROM tickets WHERE ticket_id = ?",
    (active_ticket,)
)

#fetching the ticket
ticket = cursor.fetchone()

#updating ticket
if ticket is None:
    print("Ticket not found")
elif ticket[2] == 1:
    print("Ticket already used")
else:
    cursor.execute(
        "UPDATE tickets SET used = ? WHERE ticket_id = ?",
        (1, active_ticket)
    )
    #commit new changes
    connection.commit()
    print("Ticket marked as used")

#closing connection
connection.close()