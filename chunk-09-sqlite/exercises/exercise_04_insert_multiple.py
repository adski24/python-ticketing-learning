import sqlite3

#connect to tickets.db
connection = sqlite3.connect("tickets.db")

#create a cursor
cursor = connection.cursor()

#create list with 3 tickets
tickets = [
    ("abcd", "adelina", 0),
    ("efgh", "felix", 1),
    ("ijkl", "lola", 0)
]

#inserting all tickets
cursor.executemany(
    "INSERT INTO tickets(ticket_id, customer, used) VALUES (?, ?, ?)",
    tickets
)

#commit the new changes
connection.commit()

#print confirmation
print("tickets added to the database")

#close the connection
connection.close()