valid_ticket = input("Is your ticket valid? ")
ticket_VIP = input("Are you VIP? ")
ticket_staff = input("Are you staff? ")



if valid_ticket.strip().lower() == "yes" and ticket_VIP.strip().lower() == "yes":
    print("VIP entry allowed")
elif valid_ticket.strip().lower() == "yes" and ticket_staff.strip().lower() == "yes":
    print("VIP entry allowed")
elif valid_ticket.strip().lower() == "yes" and (ticket_VIP.strip().lower() == "no" and ticket_staff.strip().lower() == "no"):
    print("VIP entry denied")
else:
    print("Entry denied")