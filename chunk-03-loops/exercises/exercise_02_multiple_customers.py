ticket_price = 25

for customer in range(5):
    customer_name = input("Enter your name: ")
    ticket_amount = int(input("Enter your ticket amount: "))
    total = ticket_amount * ticket_price
    print(f"Customer Name: {customer_name}")
    print(f"Ticket Amount: {ticket_amount}")
    print(f"Total Price: {total}")
