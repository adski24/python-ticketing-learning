# Exercise 4 — Order Total
#
# Goal:
# Combine input(), int(), variables, and arithmetic.
#
# Tasks:
# 1. Set a ticket price.
# 2. Ask how many tickets the customer wants.
# 3. Convert the input to an integer.
# 4. Calculate the order total.
# 5. Print the total.

# Write your code below:
ticket_price =  35
ticket_quantity = int(input("How many tickets would you like?"))
order_total = ticket_quantity * ticket_price

print("Total: ", order_total)
