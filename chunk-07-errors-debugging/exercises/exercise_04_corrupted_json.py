import json

try:
    with open("tickets.json", "r") as file:
        ticket = json.load(file)
        print("Ticket data loaded successfully")

except FileNotFoundError:
    print("Ticket data not found")

except json.JSONDecodeError:
    print("Ticket data is corrupted")
