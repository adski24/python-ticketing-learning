#creating ticket dictionary
tickets = [
    {
        "id": "abcd",
        "name": "adelina",
        "type": "adult",
        "cost": 25,
        "used": False
    },
    {
        "id": "efgh",
        "name": "felix",
        "type": "senior",
        "cost": 20,
        "used": False
    },
    {
        "id": "ijkl",
        "name": "lola",
        "type": "child",
        "cost": 10,
        "used": True
    },
]

used_tickets = 0
unused_tickets = 0

#ask for ticket id
active_tickets = input("What is the ticket number?").strip().lower()

#check if ticket is valid and used
for ticket in tickets:
    if active_tickets == ticket["id"]:
        if ticket["used"] == False:
            print(f'Ticket: {ticket["id"]}')
            print(f'Name: {ticket["name"]}')
            print(f'Type: {ticket["type"]}')
            print(f'Cost: {ticket["cost"]}')
            ticket["used"] = True
            print(f'Ticket {ticket["id"]} is used')
            break
        else:
            print(f'Ticket: {ticket["id"]} has already been used')
            break
else:
    print(f'Ticket: {active_tickets} does not exist')

for ticket in tickets:
    if ticket["used"] == True:
        used_tickets += 1
    else:
        unused_tickets += 1

#counting total tickets
#total_tickets = unused_tickets + used_tickets
total_tickets = len(tickets)

print(f'Total tickets: {total_tickets}')
print(f'Used tickets: {used_tickets}')
print(f'Unused tickets: {unused_tickets}')

