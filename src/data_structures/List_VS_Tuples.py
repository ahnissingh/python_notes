"""
Python: List vs Tuple - Detailed Comparison

This file explores the key differences between Lists and Tuples in Python.
It covers theoretical concepts, code examples, and practical applications.
The key differences will be highlighted for a 10-mark or 5-mark exam question.

Key Topics:
- List and Tuple Overview
- Mutability and Immutability
- Syntax Differences
- Memory Efficiency
- Performance Comparison
- Use Cases
- Methods and Operations
"""
# 1. List and Tuple Overview

# A List is a mutable, ordered collection of elements. Lists are commonly used when data needs to be changed after creation.
# A Tuple is an immutable, ordered collection of elements. Tuples are used when the data should not be changed.

# Examples of creating a list and tuple:
my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)

# 2. Mutability vs Immutability

# Lists are mutable, meaning you can modify their contents (change, add, or remove elements).
my_list[0] = 10  # Modifying an element in the list
my_list.append(5)  # Adding an element to the list
print("Modified list:", my_list)  # Output: [10, 2, 3, 4, 5]

# Tuples are immutable, meaning once created, you cannot modify their contents.
# Uncommenting the following line will raise an error:
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 3. Syntax Differences

# Lists are created using square brackets []
# Tuples are created using parentheses ()

# List Example:
my_list = [1, 2, 3, 4]
# Tuple Example:
my_tuple = (1, 2, 3, 4)

# 4. Memory Efficiency

# Tuples are more memory-efficient than lists because they are immutable and take less memory to store.
import sys

list_size = sys.getsizeof(my_list)  # Size of the list in memory
tuple_size = sys.getsizeof(my_tuple)  # Size of the tuple in memory

print(f"Memory used by list: {list_size} bytes")
print(f"Memory used by tuple: {tuple_size} bytes")

# The tuple is more memory-efficient because it doesn't need to store metadata for mutability.
# For larger datasets, tuples provide better memory utilization.

# 5. Performance Comparison

# Lists are slower than tuples because they support additional operations like adding/removing elements.
# Tuples are faster for iteration, access, and iteration because they are immutable.

import time

# Performance comparison for iteration
list_time_start = time.time()
for _ in range(1000000):
    for x in my_list:
        pass
list_time_end = time.time()

tuple_time_start = time.time()
for _ in range(1000000):
    for x in my_tuple:
        pass
tuple_time_end = time.time()

print(f"List iteration time: {list_time_end - list_time_start}")
print(f"Tuple iteration time: {tuple_time_end - tuple_time_start}")

# The tuple iteration will be faster due to its immutability and optimizations for performance.

# 6. Use Cases

# Lists are used when:
# - You need to modify the data after creation (add, remove, or change items).
# - You need dynamic data structures that change over time.
# - Example: A list of students' names in a class where the list may change.

# Tuples are used when:
# - You need to store data that should not change after creation (constant data).
# - You need to ensure the data integrity (e.g., coordinates, database records, fixed configurations).
# - Example: Storing the coordinates (x, y) of a point on a 2D plane that should not change.

# 7. Methods and Operations

# Lists have more built-in methods because they support mutability.
# Tuple methods are limited as tuples are immutable.

# List Methods:
my_list.append(6)  # Adds an item to the list
my_list.remove(2)  # Removes the first occurrence of 2
my_list.pop()  # Removes the last item of the list

# Tuple Methods:
# Tuples only have two methods: count() and index()
print("Count of 3 in tuple:", my_tuple.count(3))  # Output: 1
print("Index of 3 in tuple:", my_tuple.index(3))  # Output: 2

# Lists support all these operations: append(), extend(), insert(), remove(), pop(), reverse(), sort(), etc.
# Tuples only support count() and index(), as they are immutable.

# 8. Key Points for Exam
"""
Key differences between Lists and Tuples:

1. **Mutability**:
   - Lists are mutable, meaning elements can be changed, added, or removed.
   - Tuples are immutable, meaning once they are created, their contents cannot be changed.

2. **Syntax**:
   - Lists use square brackets [].
   - Tuples use parentheses ().

3. **Memory Efficiency**:
   - Tuples are more memory-efficient than lists, as they are immutable and require less memory to store.

4. **Performance**:
   - Tuples are generally faster for iteration and access because of their immutability.
   - Lists have more overhead due to their support for mutable operations.

5. **Use Cases**:
   - Lists are suitable when the data needs to be modified (e.g., dynamic data structures).
   - Tuples are better for data that should remain constant (e.g., coordinates, fixed configuration).

6. **Methods**:
   - Lists have a wide range of methods for adding, removing, and modifying elements.
   - Tuples have limited methods: count() and index().

7. **When to Use**:
   - Use **lists** when you need a dynamic and flexible data structure where elements might change.
   - Use **tuples** when you need to store fixed, constant data and want the benefits of immutability, like faster iteration and better memory usage.
"""

# End of List vs Tuple Learning
