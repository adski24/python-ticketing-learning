# Chunk 1 — Python Basics

## Goal

Become comfortable writing and running small Python programs while using ticketing-related examples.

---

## 1. Printing

```python
print("christmas")
```

Try changing the text and running the program again.

---

## 2. Variables

```python
event_name = "Summer Festival"
ticket_price = 35
ticket_quantity = 3
```

Python does not require you to declare variable types like C does.

---

## 3. Basic Arithmetic

```python
ticket_price = 35
ticket_quantity = 3

total = ticket_price * ticket_quantity

print(total)
```

---

## 4. User Input

```python
customer_name = input("Customer name: ")
print(customer_name)
```

Important: `input()` returns a string.

---

## 5. Type Conversion

If the user enters a number:

```python
ticket_quantity = int(input("Number of tickets: "))
```

Common conversions:

```python
int()
float()
str()
```

---

## 6. f-Strings

```python
customer_name = "Alex"
ticket_quantity = 3

print(f"{customer_name} purchased {ticket_quantity} tickets.")
```

---

## Chunk 1 Ticketing Connection

These basic values will eventually become real ticket/order data:

```text
customer name
event name
ticket quantity
ticket price
order total
```
