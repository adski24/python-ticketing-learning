import sqlite3
import qrcode
import uuid

#connect to database
connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

#id creation
ticket_id = str(uuid.uuid4())[:8]

#ask for customer name
name = input("Enter your name: ").strip().lower()

#insert ticket into database
cursor.execute("INSERT INTO tickets VALUES (?,?,?)",
               (ticket_id, name, 0)
               )
connection.commit()

#generating qr code
qr = qrcode.make(ticket_id)
filename = f"ticket_{ticket_id}.png"
qr.save(filename)
print(ticket_id)
print(filename)

connection.close()
