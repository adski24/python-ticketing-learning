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

    #adding a mark used method
    def mark_used(self):
        if self.used:
            return "Ticket already used"
        else:
            self.used = True
            return "Ticket now marked as used"

#creating a ticket
ticket1 = Ticket("abcd", "adelina", False)

result = ticket1.check_status()
result2 = ticket1.mark_used()
result3 = ticket1.check_status()

print(result)
print(result2)
print(result3)