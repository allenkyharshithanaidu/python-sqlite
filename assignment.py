import sqlite3
# Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')
# Insert data
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Alice', 85.5))
connection.commit()

# Query the database
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()