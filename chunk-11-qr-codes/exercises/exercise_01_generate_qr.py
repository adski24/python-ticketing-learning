import qrcode

ticket_id = "abcd1234"

qr = qrcode.make(ticket_id)
qr.save("ticket_abcd1234.png")

print("QR code created")