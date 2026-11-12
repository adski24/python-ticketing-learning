ticket_id = " "
ticket_counter = 0

while True:
    ticket_id = input("Enter ticket ID: ").strip()
    if ticket_id != "" and ticket_id != "quit":
        print(f"Ticket scanned: {ticket_id}")
        ticket_counter += 1
        continue
    elif ticket_id == "quit":
        break

print("Scanner closed")
print(f"Total tickets scanned: {ticket_counter}")

