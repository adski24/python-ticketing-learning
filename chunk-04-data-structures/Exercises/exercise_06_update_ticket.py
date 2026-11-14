ticket = {
    "id": "abcd",
    "customer": "john",
    "type": "adult",
    "cost": 25,
    "validity": True
}
#current ticket status
if ticket["validity"] == True:
    print("Ticket is valid")
    ticket["validity"] = False
    print(f'Ticket {ticket["id"]} has now been used')

else:
    print(f'Ticket has already been used')


