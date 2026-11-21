#creating the ticket class
class Ticket:
    def __init__(self, ticket_id, customer, used):
        self.ticket_id = ticket_id
        self.customer = customer
        self.used = used

    def check_status(self):
        if self.used:
            return "Ticket already used"
        else:
            return "Ticket not yet used"

    def mark_used(self):
        if self.used:
            return "Ticket already used"
        else:
            self.used = True
            return "Ticket now marked used"

#ask for ticket id
active_ticket = input("Enter ticket ID: ").strip().lower()

#current tickets
ticket1 = Ticket("abcd", "adelina", True)
ticket2 = Ticket("efgh", "felix", False)
ticket3 = Ticket("ijkl", "lola", False)

tickets = [ticket1, ticket2, ticket3]

for ticket in tickets:
    if active_ticket == ticket.ticket_id:
        print(ticket.customer, ticket.check_status())
        if ticket.used:
            print("Ticket already used")
            break
        else:
            result = ticket.mark_used()
            print(result)
            print(ticket.check_status())
            break
else:
    print("Ticket not found")

