import json

try:
    with open("tickets.json", "r") as file:
        tickets = json.load(file)
        print("Ticket data loaded")

except FileNotFoundError:
    print("File not found")