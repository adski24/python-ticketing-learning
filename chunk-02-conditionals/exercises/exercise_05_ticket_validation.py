ticket_existing = input("Does the ticket exist? ").strip().lower()
ticket_valid = input("Is the ticket valid? ").strip().lower()
ticket_used = input("Has the ticket been used ").strip().lower()

if ticket_existing == "no":
    print("Invalid ticket")
elif ticket_existing == "yes" and ticket_valid == "no":
    print("Ticket rejected")
elif ticket_existing == "yes" and ticket_valid == "yes" and ticket_used == "yes":
    print("Ticket already used")
else:
    print("Entry allowed")