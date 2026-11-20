class Ticket:
    def __init__(self, ticket_id, customer, used):
        self.ticket_id = ticket_id
        self.customer = customer
        self.used = used

    #adding a method
    def check_status(self):
        if self.used:
            return "Ticket already used"
        else:
            return "Ticket not used"

#create a ticket
ticket1 = Ticket("abcd", "adelina", True)

#call the method
result = ticket1.check_status()
print(result)
