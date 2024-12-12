import shelve

# Open a shelve file (it creates the file if it doesn't exist)
with shelve.open('my_shelf.db') as shelf:

    # Writing data to the shelf
    shelf['name'] = 'Alice'
    shelf['age'] = 30
    shelf['is_student'] = False

    # Reading data from the shelf
    print("Name:", shelf['name'])
    print("Age:", shelf['age'])
    print("Is Student:", shelf['is_student'])

    # Updating existing data
    shelf['age'] = 31
    print("Updated Age:", shelf['age'])

    # Deleting data from the shelf
    del shelf['is_student']
    print("Is Student after deletion:", 'is_student' in shelf)  # Should print False

# At this point, the shelve file 'my_shelf.db' contains the data.
