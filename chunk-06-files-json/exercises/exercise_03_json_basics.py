import json

ticket = {
    "id": "abcd",
    "customer": "adelina",
    "used": False
}

with open("ticket.json", "w") as file:
    json.dump(ticket, file)