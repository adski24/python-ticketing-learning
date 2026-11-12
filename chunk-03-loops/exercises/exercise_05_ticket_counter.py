ticket_ID = " "
ticket_counter = 0
while ticket_ID != "quit":
    ticket_ID = input("Enter ticket ID: ").strip()
    if ticket_ID != "" and ticket_ID != "quit":
        print(f"Ticket scanned: {ticket_ID}")
        ticket_counter += 1
        continue
    elif ticket_ID == "quit":
        break


print("Scanner closed")
print(f' Total tickets scanned: {ticket_counter}')

