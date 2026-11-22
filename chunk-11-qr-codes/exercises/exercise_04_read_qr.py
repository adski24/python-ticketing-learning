from PIL import Image
from pyzbar.pyzbar import decode

image = Image.open("ticket_abcd1234.png")
decoded_object = decode(image)

#extract the ticket_id
for result in decoded_object:
    ticket_id = result.data.decode("utf-8")
    print(ticket_id)