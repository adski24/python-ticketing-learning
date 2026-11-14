#list of tickets
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

#search for the ticket id
for ticket in tickets:
    #check if ticket id exists
    if active_ticket == ticket["id"]:
        #check if ticket is used
        if ticket["used"] == True:
            print(f'Ticket ID: {ticket["id"]} is used')
            break
        else:
            ticket["used"] = True
            print(f'Ticket ID: {ticket["id"]}')
            print(f'Customer: {ticket["customer"]}')
            print(f'Type: {ticket["type"]}')
            print(f'Ticket Price: {ticket["price"]}')
            print(f'Ticket {ticket["id"]} has now been used.')
            break
else:
    print(f'Ticket ID: {active_ticket} does not exist')
