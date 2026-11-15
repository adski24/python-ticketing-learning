ticket = {
    "id": "abcd",
    "customer": "adelina",
    "used": False
}

def mark_ticket_used(ticket):
    if ticket is None:
        return "Ticket not found"
    elif ticket["used"]:
        return "Ticket already used"
    else:
        ticket["used"] = True
        return "Ticket marked as used"

result = mark_ticket_used(ticket)
print(result)
print(ticket)