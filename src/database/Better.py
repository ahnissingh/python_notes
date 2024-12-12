import MySQLdb
from MySQLdb import Error

# Step 1: Connecting to the MySQL database
try:
    db = MySQLdb.connect(
        host='localhost',        # MySQL host (localhost in your case)
        user='root',             # Your MySQL username
        password='root',         # Your MySQL password
        database='python',       # The name of your database
        port=3306                # Explicitly mention the port (default MySQL port)
    )
    print("Connected to the database successfully.")
except Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# Step 2: Create a cursor object
cursor = db.cursor()

# Step 3: Create a table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
    """)
    print("Table 'students' created or already exists.")
except Error as e:
    print(f"Error creating table: {e}")

# Step 4: Inserting data into the table (using parameterized queries to avoid SQL injection)
try:
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 25))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Bob", 23))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Charlie", 22))
    db.commit()  # Committing the transaction
    print("Data inserted successfully.")
except Error as e:
    print(f"Error inserting data: {e}")
    db.rollback()  # If an error occurs, rollback the transaction

# Step 5: Selecting data from the table
try:
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()  # Fetch all rows from the result set
    print("\nStudents in the database:")
    for row in rows:
        print(row)
except Error as e:
    print(f"Error fetching data: {e}")

# Step 6: Updating data in the table
try:
    cursor.execute("UPDATE students SET age = %s WHERE name = %s", (26, "Alice"))
    db.commit()  # Committing the transaction
    print("\nData updated successfully.")
except Error as e:
    print(f"Error updating data: {e}")
    db.rollback()  # Rollback if something goes wrong

# Step 7: Deleting data from the table
try:
    cursor.execute("DELETE FROM students WHERE name = %s", ("Charlie",))
    db.commit()  # Committing the transaction
    print("\nData deleted successfully.")
except Error as e:
    print(f"Error deleting data: {e}")
    db.rollback()  # Rollback if something goes wrong

# Step 8: Using Transactions (Commit and Rollback)
try:
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("David", 27))
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Eva", 28))
    # Simulating an error (we're trying to insert a duplicate id)
    cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Eva", 28))
    # This should fail due to duplicate primary key
    db.commit()  # Committing the transaction
    print("Transaction committed.")
except Error as e:
    print(f"Error during transaction: {e}")
    db.rollback()  # Rollback in case of an error

# Step 9: Handling exceptions and closing the connection
try:
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nStudents after all operations:")
    for row in rows:
        print(row)
except Error as e:
    print(f"Error during final fetch: {e}")
finally:
    # Closing cursor and connection
    cursor.close()
    db.close()
    print("\nConnection closed.")
