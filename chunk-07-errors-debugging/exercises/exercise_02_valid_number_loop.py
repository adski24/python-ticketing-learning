while True:
    try:
        ticket_number = int(input("Enter ticket quantity: "))
        print("Ticket quantity:", ticket_number)
        break
    except ValueError:
        print("Please enter a valid ticket quantity")
