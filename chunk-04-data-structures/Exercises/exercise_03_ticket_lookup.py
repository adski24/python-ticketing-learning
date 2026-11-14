#list of tickets
tickets = ["abcd", "efgh", "ijkl", "mnop", "pqrs", "tuv", "wxyz"]

#asking the user for a ticket
active_ticket = input("Enter ticket number: ").strip()

#checking if ticket is in list
if active_ticket in tickets:
    print("Ticket number found!")
else:
    print("Ticket number not found!")