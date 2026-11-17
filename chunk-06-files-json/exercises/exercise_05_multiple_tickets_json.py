import json

#dictionaries
tickets = [
    {
    "id": "abcd",
    "customer": "adelina",
    "used": False
    },
    {
    "id": "efgh",
    "customer": "felix",
    "used": True
    },
    {
    "id": "ijkl",
    "customer": "lola",
    "used": False
    }
]

with open("tickets.json", "w") as file:
    json.dump(tickets, file)

with open("tickets.json", "r") as file:
    content = json.load(file)

for ticket in content:
    print(ticket["id"])
    print(ticket["customer"])