import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a table
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (name TEXT, age INTEGER)')

# Insert some data
# cursor.execute('INSERT INTO users VALUES ("John", 20)')
# cursor.execute('INSERT INTO users VALUES ("Bob", 25)')


# Commit the changes
conn.commit()

# Close the connection
conn.close()