import json

with open("ticket.json", "r") as file:
    content = json.load(file)

print(content)
print(content["id"])
print(content["customer"])