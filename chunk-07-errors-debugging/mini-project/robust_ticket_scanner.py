import json

data_loaded = False

#loading the ticket dictionary
try:
    with open("tickets.json", "r") as file:
        tickets = json.load(file)
        data_loaded = True
except UnicodeDecodeError:
    print("Ticket data is corrupted")
except FileNotFoundError:
    print("Ticket data cannot be found")


#reject blank tickets
while True:
    # ask for ticket number
    active_ticket = input("Enter ticket number: ").strip().lower()
    if active_ticket == "":
        print("Ticket cannot be empty")
        continue
    else:
        break

#search for ticket
if data_loaded:
    for ticket in tickets:
        if active_ticket == ticket["id"]:
            if ticket["used"]:
                print("Ticket has already been used")
                break
            else:
                ticket["used"] = True
                print("Ticket is now marked as used")
                with open("tickets.json", "w") as file:
                    json.dump(tickets, file)
                    print("Tickets list has been updated")
                break
    else:
        print("Ticket not found")
