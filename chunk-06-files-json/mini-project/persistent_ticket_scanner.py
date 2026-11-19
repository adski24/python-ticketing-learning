import json

#loading the json
with open("tickets.json", "r") as file:
    tickets = json.load(file)

#ask for ticket
active_ticket = input("Enter ticket number: ").strip().lower()

#initial ticket found statea
used_tickets = 0
unused_tickets = 0

#search for ticket
for ticket in tickets:
    if active_ticket == ticket["id"]:
        if not ticket["used"]:
            ticket["used"] = True
            print("Ticket has been marked as used")
            # save updates to the dictionary
            with open("tickets.json", "w") as file:
                json.dump(tickets, file)
                print("Ticket has been saved")
                break
        else:
            print("Ticket already used")
            break
else:
    print("Ticket not found")

#counting used and unused tickets
for ticket in tickets:
    if ticket["used"]:
        used_tickets += 1
    else:
        unused_tickets += 1

total_tickets = len(tickets)
print("Total tickets: ", total_tickets)
print("Used tickets: ", used_tickets)
print("Unused tickets: ", unused_tickets)
print(tickets)


