ticket = {
    "id": "abcd",
    "customer": "adelina",
    "used": True
}

def validate_ticket(ticket):
    if ticket is None:
        return "Ticket not found"
    elif not ticket["used"]:
        return "Entry allowed"
    else:
        return "Ticket already used"

result = validate_ticket(ticket)
print(result)
