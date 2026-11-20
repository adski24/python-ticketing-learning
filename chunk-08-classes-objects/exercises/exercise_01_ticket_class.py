class Ticket:
    def __init__(self, ticket_id, customer, used):
        self.ticket_id = ticket_id
        self.customer = customer
        self.used = used

#creating a ticket
ticket1 = Ticket("abcd", "adelina", False)

#accessing the data
print(ticket1.ticket_id)
print(ticket1.customer)
print(ticket1.used)