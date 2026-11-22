import requests

#asking for input
ticket_id = input("Enter your ticket ID: ").strip().lower()
customer = input("Enter your name: ").strip().lower()

#create a dictionary
ticket_data = {
    "ticket_id": ticket_id,
    "customer": customer,
    "used": False
}

#send the ticket request
response =requests.post("https://httpbin.org/post", json=ticket_data)

#print the status code
print(response.status_code)

#convert to json and print
data = response.json()
print(data["json"])

