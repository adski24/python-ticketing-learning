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
#ask for the ticket id
active_ticket = input("Enter ticket ID: ").strip().lower()

#check if ticket is in list
for ticket in tickets:
    if active_ticket == ticket["id"]:
        print(f'Ticket: {ticket["id"]}')
        print(f'Customer: {ticket["customer"]}')
        print(f'Price: {ticket["price"]}')
        print(f'Used: {ticket["used"]}')
        print(f'Type: {ticket["type"]}')
        break
else:
    print("Ticket not found")