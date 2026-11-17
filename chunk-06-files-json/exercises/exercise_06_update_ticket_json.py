import json

#load the tickets
with open("tickets.json", "r") as file:
    tickets_list = json.load(file)

#ask for ticket input
active_ticket = input("Enter ticket ID: ").strip().lower()

#search for ticket
ticket_found = False

for ticket in tickets_list:
    if active_ticket == ticket["id"]:
        ticket_found = True

        if not ticket["used"]:
            ticket["used"] = True
            print("Ticket marked as used")
        else:
            print("Ticket already used")
            break

if not ticket_found:
    print("Ticket not found")


#save updated tickets
with open("tickets.json", "w") as file:
    json.dump(tickets_list, file)
    if ticket["used"]:
        print("Ticket updated")