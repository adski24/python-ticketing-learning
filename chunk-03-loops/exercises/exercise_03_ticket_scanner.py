ticket_ID = ""
while ticket_ID != "quit":
    ticket_ID = input("Enter ticket ID: ")
    if ticket_ID != "quit":
        print(f"Ticket scanned: {ticket_ID}")

print("Scanner closed")
