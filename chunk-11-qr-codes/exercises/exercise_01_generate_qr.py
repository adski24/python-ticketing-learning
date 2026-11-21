import qrcode

ticket_id = "abcd1234"

qr = qrcode.make(ticket_id)
qr.save("ticket_qr.png")

print("QR code created")