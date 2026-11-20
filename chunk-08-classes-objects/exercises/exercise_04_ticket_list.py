class Ticket:
    def __init__(self, id, name, used):
        self.id = id
        self.name = name
        self.used = used


    def check_status(self):
        if self.used:
                return "Ticket already used"
        else:
                return "Ticket not used"

#creating tickets
ticket1 = Ticket("abcd", "adelina", True)
ticket2 = Ticket("efgh", "felix", False)
ticket3 = Ticket("ijkl", "lola", False)

tickets = [ticket1, ticket2, ticket3]

for ticket in tickets:
        print(ticket.id, ticket.name, ticket.check_status())