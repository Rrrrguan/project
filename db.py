import sqlite3

# Connect to or create a new SQLite database file
conn = sqlite3.connect('demo.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS demo (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        published_year INTEGER
    )
''')
conn.commit()

# Insert data into the table
cursor.execute("INSERT INTO demo (title, author, published_year) VALUES (?, ?, ?)",
               ("Sample Book", "John Doe", 2022))

# Commit the changes to the database

conn.commit()