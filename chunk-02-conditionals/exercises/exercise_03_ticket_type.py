age = int(input("How old are you?: "))

if age < 12:
    ticket_price = 10
    ticket_type = "Child"
elif age <= 64:
    ticket_price = 20
    ticket_type = "Adult"
else:
    ticket_price = 15
    ticket_type = "Senior"

print(f"Ticket type: {ticket_type}, Total price: {ticket_price:.2f}")
