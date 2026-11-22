import sqlite3
import qrcode
import uuid
from PIL import Image
from pyzbar.pyzbar import decode

#ask for customer name
name = input("Enter your name: ").strip().lower()

#connect to database
connection = sqlite3.connect("chunk-11-qr-codes/exercises/tickets.db")
cursor = connection.cursor()

#check for uniqueness
while True:
    #generate unique id
    ticket_id = str(uuid.uuid4())[:8]

    cursor.execute(
        "SELECT * FROM tickets WHERE ticket_id = ?",
        (ticket_id,)
    )

    existing_ticket = cursor.fetchone()

    #check if ticket exists
    if existing_ticket is None:
        break

#save ticket in database
cursor.execute(
    "INSERT INTO tickets VALUES (?,?, ?)",
    (ticket_id, name, 0)
)
connection.commit()

ticket_qr = qrcode.make(ticket_id)
filename = f"ticket_{ticket_id}.png"
ticket_qr.save(filename)

#read and decode image
image = Image.open(filename)
decoded_qr = decode(image)

#print decoded id
for result in decoded_qr:
    decoded_id = result.data.decode("utf-8")
    print(decoded_id)

connection.close()