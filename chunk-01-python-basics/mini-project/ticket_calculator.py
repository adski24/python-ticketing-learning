# Chunk 1 Mini-Project — Ticket Price Calculator
#
# Build this yourself using the concepts from Chunk 1.
#
# Required program behavior:
#
# 1. Store an event name.
# 2. Store the price of one ticket.
# 3. Ask the customer for their name.
# 4. Ask how many tickets they want.
# 5. Calculate the total.
# 6. Print a clean order summary.
#
# Target output:
#
# ------ ORDER ------
# Event: Summer Festival
# Customer: Adelina
# Tickets: 3
# Price per ticket: $35
# Total: $105
# -------------------
#
# Optional challenge:
# Ask the user for the ticket price instead of hard-coding it.
#
# IMPORTANT:
# Try to complete this without looking up a full solution.
# If you get stuck, ask for a hint rather than the finished code.


# Start your program below:
#initializing variables
event_name = "Christmas Party"
event_date = "December 12, 2026"

#ask for customer details
customer_name = input("Customer name: ")
ticket_quantity = int(input("Ticket quantity: "))
ticket_price = int(input("Ticket price: "))

total_price = ticket_quantity * ticket_price

#order
print(f"Event name: {event_name}")
print(f"Event date: {event_date}")
print(f"Customer name: {customer_name}")
print(f"Number of tickets: {ticket_quantity}")
print(f"Ticket price: {ticket_price}")
print(f"Total price: {total_price}")
