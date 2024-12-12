import MySQLdb

# Connect to the MySQL database
db = MySQLdb.connect(
    host='localhost',        # MySQL host (localhost in your case)
    user='root',             # Your MySQL username
    password='root',         # Your MySQL password
    database='python',       # The name of your database
    port=3306                # Explicitly mention the port (default MySQL port)
)

# Create a cursor object
cursor = db.cursor()

# Create the 'students' table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
""")
# Check if the 'students' table has data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# If no rows are returned, insert some sample data
if len(rows) == 0:
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 25))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Bob", 23))
    db.commit()  # Commit the changes

# Fetch all rows from the 'students' table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Print the rows fetched from the table
print("Before Update:")
for row in rows:
    print(row)

# Update the age of Alice to 26
cursor.execute("UPDATE students SET age = %s WHERE name = %s", (26, "Alice"))
db.commit()  # Commit the changes

# Fetch the updated rows
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Print the updated rows
print("\nAfter Update:")
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()
