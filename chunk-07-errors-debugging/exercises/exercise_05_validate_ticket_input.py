while True:
        try:
            ticket_number = input("Enter a ticket number: ").strip().lower()
            if ticket_number != "":
                print("The ticket number is: ", ticket_number)
                break
        except ValueError:
            print("The ticket can't be empty")
