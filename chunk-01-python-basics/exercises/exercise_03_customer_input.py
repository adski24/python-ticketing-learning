# Exercise 3 — Customer Input
#
# Goal:
# Practice input(), strings, and type conversion.
#
# Tasks:
# 1. Ask the customer for their name.
# 2. Ask how many tickets they want.
# 3. Store both answers in variables.
# 4. Print the customer's name and requested quantity.
#
# Remember:
# input() returns a string.
# If you need a number, convert it.

# Write your code below:
customer_name = input("Customer name: ")
customer_tickets = int(input("Number of tickets: "))

print("Name:", customer_name, "Tickets:", customer_tickets)