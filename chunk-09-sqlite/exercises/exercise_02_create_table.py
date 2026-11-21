import sqlite3

connection = sqlite3.connect("tickets.db")
cursor = connection.cursor()

#creating a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets( 
    ticket_id TEXT, 
    customer TEXT,
    used INTEGER
) 
""")
connection.commit()
connection.close()
