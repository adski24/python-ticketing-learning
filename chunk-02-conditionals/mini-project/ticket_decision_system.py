# customer information
customer_age = int(input("Enter customer age: "))

# ticket pricing
if customer_age < 12:
    ticket_price = 10
    ticket_type = "Child"
elif customer_age <=64:
    ticket_price = 20
    ticket_type = "Adult"
else:
    ticket_price = 15
    ticket_type = "Senior"

# discount calculation
ticket_count =  int(input("Enter ticket amount: "))
total_price = ticket_price * ticket_count

# ticket validation
ticket_exist = input("Does the ticket exist?: ").strip().lower()
ticket_valid = input("Is the ticket valid?: ").strip().lower()
ticket_used = input("Has the ticket been used?: ").strip().lower()

# output
print("-----ORDER-----")
print(f"Ticket Type: {ticket_type}")
print(f"Ticket Quantity: {ticket_count}")
print(f"Price per ticket: {ticket_price}")

if ticket_count >= 10:
    discounted_price = total_price * 0.9
    print(f"Total price: {discounted_price}")
else:
    print(f"Total price: {total_price}")

print("---------------")
print("-----ENTRY CHECK-----")
if ticket_exist == "no":
    print("Entry not allowed")
elif ticket_valid == "no":
    print("Invalid ticket")
elif ticket_used == "yes":
    print("Ticket already used")
else:
    print("Entry allowed")
print("---------------------")
