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
    }
]

#asking for the ticket
active_ticket = input("What is the ticket number?: ")

#creating the function for searching for ticket
def find_ticket(tickets, active_ticket):
    for ticket in tickets:
        if active_ticket == ticket["id"]:
            #print("Ticket found")
            return ticket
    else:
        #print("Ticket not found")
        return None

found_ticket = find_ticket(tickets, active_ticket)

#creating the validating function
def validate_ticket(found_ticket):
    if found_ticket is None:
        return "Ticket not found"
    elif found_ticket["used"]:
        return "Ticket already used"
    else:
        return "Entry valid"

#creating the marking function
def mark_ticket_used(found_ticket):
    if not found_ticket["used"]:
        found_ticket["used"] = True
        return found_ticket
    else:
        return None

validated_ticket = validate_ticket(found_ticket)
print(validated_ticket)

if validated_ticket == "Entry valid":
    mark_ticket_used(found_ticket)
    print("Ticket marked as used")