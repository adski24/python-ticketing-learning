tickets = [
    {
        "id": "abcd",
        "type": "adult",
        "customer": "adelina",
        "price": 25,
        "used": False
    },

    {
        "id": "efgh",
        "type": "child",
        "customer": "felix",
        "price": 10,
        "used": True
    },

    {
        "id": "ijkl",
        "type": "senior",
        "customer": "lola",
        "price": 15,
        "used": True
    }
]

for ticket in tickets:
    print(f'Ticket ID: {ticket["id"]}')
    print(f'Customer: {ticket["customer"]}')
    print(f'Type: {ticket["type"]}')
    print(f'Price: {ticket["price"]}')
    print(f'Used: {ticket["used"]}')
    print("")
