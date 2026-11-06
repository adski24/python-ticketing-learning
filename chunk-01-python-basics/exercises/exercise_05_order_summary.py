# Exercise 5 — Order Summary
#
# Goal:
# Practice f-strings and combining everything from Chunk 1.
#
# Ask for:
# - customer name
# - number of tickets
#
# Store:
# - event name
# - ticket price
#
# Calculate:
# - order total
#
# Print something similar to:
#
# ------ ORDER ------
# Event: Summer Festival
# Customer: Alex
# Tickets: 4
# Price per ticket: $35
# Total: $140
# -------------------

# Write your code below:
customer_name = input("Customer name: ")
ticket_quantity = int(input("How many tickets would you like: "))

event_name = "Gala"
event_date = "June 2, 2027"

ticket_price = 20
total_price = ticket_quantity * ticket_price

print(f"Customer: {customer_name} Event: {event_name} Date: {event_date} Tickets: {ticket_quantity} Price: {ticket_price} Total: {total_price}")