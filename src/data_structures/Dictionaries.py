"""
Python: Dictionaries (Maps) - In-depth Study

This file provides a detailed explanation of Python Dictionaries, including their internal working,
hash table implementation, and key concepts. This explanation is intended to help with exam preparation,
especially for questions about dictionaries, their performance, and their use cases.

Key Topics:
- Introduction to Hash Tables and their relationship to Dictionaries
- Internal Working of Python Dictionaries
- Syntax and Basic Operations on Dictionaries
- Dictionary Methods and Operations
- Performance Analysis
- Use Cases
"""

# 1. Introduction to Hash Tables and Their Relation to Dictionaries

# A **Hash Table** is a data structure that stores key-value pairs. In a hash table, a hash function is used
# to compute an index (or hash code) for a given key, which determines where the corresponding value will
# be stored. This allows for efficient retrieval of values based on the key.

# **Hash Table Structure:**
# - **Key**: The unique identifier used to look up a value.
# - **Value**: The data associated with the key.
# - **Hash Function**: A function that converts a key into an index (or hash code), which is used to store
#   the value in an array-like structure.
# - **Collision Handling**: When two keys hash to the same index, a collision occurs, and methods like
#   chaining or open addressing are used to resolve the collision.

# Python's **Dictionary** is implemented using a hash table under the hood. When a key-value pair is inserted
# into a dictionary, Python applies a hash function to the key to determine where to store the value.
# This allows for fast lookups, insertions, and deletions, typically in **O(1)** time complexity.

# Example of hash table behavior (simplified):
# Let's consider inserting a key-value pair into a hash table:
# Key: 'name', Value: 'Alice'

# Internally:
# 1. A hash function is applied to the key 'name'.
# 2. The hash function computes an index (e.g., 2).
# 3. The value 'Alice' is stored at index 2 in the hash table.

# 2. Internal Working of Python Dictionaries

# Python dictionaries are implemented using **open addressing** for collision resolution and a **dynamic array**
# for storage. When a key-value pair is inserted, Python calculates the hash code of the key and looks for the
# corresponding index in the internal array. If the slot is already occupied (collision), Python will probe the
# next available slot, either linearly or using a quadratic method.

# **Key Components:**
# 1. **Hashing**: Python applies a built-in hash function to the key to get a hash code, which is used to compute
#    the index where the value should be stored.
# 2. **Collisions**: When two keys have the same hash code (hash collision), Python uses open addressing to find
#    the next available spot in the dictionary's internal array.
# 3. **Resizing**: As the dictionary grows, the size of the internal array increases. Python automatically resizes
#    the array when the dictionary becomes too large, maintaining the **load factor** for optimal performance.

# **Example of Insertion:**
# Creating a dictionary with some key-value pairs:
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# When 'name' is inserted:
# - Python hashes the key 'name'.
# - It calculates an index for 'name' and stores the value 'Alice' at that index in the internal array.

# If 'age' is inserted:
# - Python hashes the key 'age' and calculates a different index (based on the hash function).
# - It stores the value '25' at the calculated index.

# **Resizing Example**:
# If the dictionary grows too large and exceeds the threshold, Python will create a new, larger internal array
# and rehash all existing key-value pairs into the new array to maintain efficient lookup times.

# 3. Syntax and Basic Operations on Dictionaries

# Syntax for creating a dictionary:
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Accessing values:
print(my_dict['key1'])  # Output: 'value1'

# Adding or updating values:
my_dict['key3'] = 'value3'  # Adds a new key-value pair
my_dict['key1'] = 'updated_value1'  # Updates the value of 'key1'

# Deleting a key-value pair:
del my_dict['key2']  # Removes the key-value pair for 'key2'

# 4. Dictionary Methods and Operations

# 1. **get()**: Retrieve the value for a given key, returning None if the key is not found.
print(my_dict.get('key1'))  # Output: 'updated_value1'
print(my_dict.get('key4'))  # Output: None

# 2. **keys()**: Returns a view object of all keys in the dictionary.
print(my_dict.keys())  # Output: dict_keys(['key1', 'key3'])

# 3. **values()**: Returns a view object of all values in the dictionary.
print(my_dict.values())  # Output: dict_values(['updated_value1', 'value3'])

# 4. **items()**: Returns a view object of all key-value pairs as tuples.
print(my_dict.items())  # Output: dict_items([('key1', 'updated_value1'), ('key3', 'value3')])
#4.1 Traversing items
for key , value in my_dict.items():
    print(f"{key} : {value}")


# 5. **pop()**: Removes a key-value pair and returns the value.
print(my_dict.pop('key1'))  # Output: 'updated_value1'

# 6. **clear()**: Removes all key-value pairs from the dictionary.
my_dict.clear()  # Clears the dictionary

# 7. **update()**: Merges another dictionary into the current dictionary.
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

# 5. Performance Analysis

# Dictionary operations (insertion, lookup, deletion) typically have an **average time complexity of O(1)**.
# However, in cases of hash collisions or when the dictionary needs to be resized, the complexity can degrade
# to O(n). Python tries to minimize the likelihood of such performance degradation.

# **Time Complexity Breakdown**:
# - **Accessing a value** by key (e.g., my_dict[key]) takes O(1) on average.
# - **Inserting** a new key-value pair takes O(1) on average.
# - **Deleting** a key-value pair takes O(1) on average.
# - **Iterating** over keys/values/items takes O(n) where n is the number of key-value pairs.

# 6. Use Cases

# Dictionaries are ideal when:
# - You need fast lookups by key.
# - You need a collection of unique keys with associated values.
# - Example: Storing student IDs as keys and student details (name, age, etc.) as values.

# Dictionaries are not suitable when:
# - You need ordered collections (before Python 3.7, dictionaries were unordered; after Python 3.7, they maintain insertion order).

# Example Use Case:
# Storing employee details:
employee_dict = {
    'emp1': {'name': 'John', 'age': 30, 'department': 'HR'},
    'emp2': {'name': 'Jane', 'age': 25, 'department': 'Finance'}
}

# 7. Key Points for Exam

"""
Key Characteristics of Python Dictionaries:
By default, Python dictionaries dynamically resize when the 
load factor reaches a certain threshold (around 2/3, 
or approximately 66%), though this threshold 
and the underlying resizing strategy are not directly
exposed for customization.

1. **Hash Table Implementation**:
   - Python dictionaries are implemented using hash tables, which provide efficient lookups, insertions, and deletions.
   - A hash function maps keys to indices in the dictionary's internal array.

2. **Mutability**:
   - Dictionaries are mutable, meaning you can modify, add, or delete key-value pairs.

3. **Unordered (Before Python 3.7)**:
   - Dictionaries in Python 3.6 and earlier do not guarantee order of key-value pairs.
   - From Python 3.7 onwards, dictionaries maintain insertion order.

4. **Performance**:
   - Dictionary operations typically have an average time complexity of O(1).
   - In cases of hash collisions or resizing, the time complexity can degrade to O(n).

5. **Methods**:
   - Common methods include `get()`, `keys()`, `values()`, `items()`, `pop()`, `update()`, and `clear()`.

6. **Use Cases**:
   - Use dictionaries for fast lookups and when you need key-value mappings (e.g., storing data in databases, configurations, etc.).
"""

# End of Dictionary (Maps) Learning
my_dict = {
    'name': 'Ahnis',
    'password': 'root',
    'cake': 'large'
}
chai_types = {
    'Masala': 'Spicy',
    'Ginger': 'Zesty',
    'Green': 'Mild'
}
# 1 )
# ZIP OPERATOR
key_values_pairs = zip(my_dict.keys(), my_dict.values())
for key, value in key_values_pairs:
    print(f"Key {key} Value {value}")
# 2
for key, value in chai_types.items():
    print(f"{key} : {value}")
# 3
for key in chai_types:
    print(key, chai_types[key])

if "Masala" in chai_types:
    print("I have masala chai")
# Pop last
chai_types.popitem()
# Pop specific
chai_types.pop('Ginger')
print(chai_types)

del chai_types['Masala']
# Nested Dictionaries
tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty",
        "Green": "Fresh",
        "Black": "Strong",
    },
    "Food":
        {
            "Petty": "Delicious",
            "Samosa": "Aaloo",
        }
}
# Dictionary Comprehension
squared_even_numbers = {x: x ** 2 for x in range(0, 11, 2)}
print(squared_even_numbers)

keys = ['Masala', 'Ginger', 'Lemom']
default_value = 'Delicious'
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
