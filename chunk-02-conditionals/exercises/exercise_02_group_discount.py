ticket_price = 35
ticket_quantity = int(input("Enter ticket quantity: "))

total_price = ticket_quantity * ticket_price

if ticket_quantity >= 10:
    discount_total = 0.9 * total_price
    print(f"Total price: ${discount_total:.2f}")
else:
    print(f"Total price: ${total_price:.2f}")