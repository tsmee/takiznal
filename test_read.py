# Connect to the database
import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor
cursor = conn.cursor()

# Execute the SELECT query
cursor.execute('SELECT * FROM users')

# Fetch all the results
results = cursor.fetchall()

# Print out the results
for result in results:
    print(result)

# Close the connection
conn.close()