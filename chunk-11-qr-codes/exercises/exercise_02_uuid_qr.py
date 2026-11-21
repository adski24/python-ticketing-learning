import uuid
import qrcode

ticket_id = str(uuid.uuid4())[:8]
qr = qrcode.make(ticket_id)

#saving the qrcode
filename = f"ticket_{ticket_id}.png"
qr.save(filename)
print(ticket_id)