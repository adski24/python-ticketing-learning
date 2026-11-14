#initiating variables
used_tickets = 0
unused_tickets = 0

#dictionary of tickets
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
    if ticket["used"] == True:
        used_tickets += 1
    else:
        unused_tickets += 1

total_tickets = len(tickets)

print(f'Total tickets: {total_tickets}')
print(f'Used tickets: {used_tickets}')
print(f'Unused tickets: {unused_tickets}')

