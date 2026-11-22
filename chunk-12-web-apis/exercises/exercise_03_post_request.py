import requests

#creating the ticket data dictionary
ticket_data = {
    "ticket_id": "abcd1234",
    "customer": "adelina",
    "used": False
}
#send the ticket
response = requests.post("https://httpbin.org/post", json=ticket_data)

print(response.status_code)

data = response.json()
print(data["json"])