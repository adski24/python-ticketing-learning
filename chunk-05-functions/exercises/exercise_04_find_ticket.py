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
def find_ticket(tickets, search_id):
    for ticket in tickets:
        if search_id == ticket["id"]:
            return ticket
    else:
        return None

result = find_ticket(tickets, "sdfghj")
print(result)