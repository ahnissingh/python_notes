"""
Python List Learning - Comprehensive Guide

This Python file covers all essential concepts related to lists.
It includes list creation, indexing, slicing, methods, and more.
This is a one-stop guide for understanding lists in Python.

Key Topics:
- List Creation
- Indexing and Slicing
- List Methods
- List Operations
- Nested Lists
- List Comprehension
- List Mutability
"""

# 1. List Creation
# A list in Python is created using square brackets [] and can contain elements of any data type (int, str, float, etc.)
empty_list = []  # Empty list
list_of_numbers = [1, 2, 3, 4, 5]  # List of integers

list_of_strings = ["apple", "banana", "cherry"]  # List of strings
mixed_list = [1, "apple", 3.14, True]  # Mixed data types

# 2. List Indexing and Slicing
# Lists are indexed starting from 0, and you can access elements using positive or negative indices.
# Negative indexing starts from -1 (last element).
print("First element:", list_of_numbers[0])  # Output: 1 (first element)
print("Last element:", list_of_numbers[-1])  # Output: 5 (last element)

# List slicing allows extracting parts of a list using the syntax list[start:end:step].
# Syntax: list[start:end:step]

sublist = list_of_numbers[1:4]  # Extracts elements from index 1 to 3 (4 is excluded)
print("List slicing (1:4):", sublist)  # Output: [2, 3, 4]

# Using step to skip elements
sublist_with_step = list_of_numbers[::2]  # Skips every second element
print("List slicing with step:", sublist_with_step)  # Output: [1, 3, 5]

# 3. List Methods
# Python provides a variety of built-in methods for manipulating lists.

# Append an element to the list
list_of_numbers.append(6)
print("After append:", list_of_numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Insert an element at a specific index
list_of_numbers.insert(2, 10)  # Inserts 10 at index 2
print("After insert:", list_of_numbers)  # Output: [1, 2, 10, 3, 4, 5, 6]

# Remove the first occurrence of an element
list_of_numbers.remove(10)
print("After remove:", list_of_numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Pop an element from a specific index (removes and returns it)
popped_element = list_of_numbers.pop(3)
print("Popped element:", popped_element)  # Output: 4
print("After pop:", list_of_numbers)  # Output: [1, 2, 3, 5, 6]

# Find the index of the first occurrence of an element
index_of_5 = list_of_numbers.index(5)
print("Index of 5:", index_of_5)  # Output: 3

# Count the occurrences of an element
count_of_3 = list_of_numbers.count(3)
print("Count of 3:", count_of_3)  # Output: 1

# Sort the list in ascending order
list_of_numbers.sort()
print("After sort:", list_of_numbers)  # Output: [1, 2, 3, 5, 6]

# Reverse the order of the list
list_of_numbers.reverse()
print("After reverse:", list_of_numbers)  # Output: [6, 5, 3, 2, 1]

# Copy the list
copied_list = list_of_numbers.copy()
print("Copied list:", copied_list)  # Output: [6, 5, 3, 2, 1]

# 4. List Operations
# Lists support various operations such as concatenation, repetition, and more.

# List Concatenation: combining two lists using '+'
new_list = list_of_numbers + [7, 8]
print("Concatenated list:", new_list)  # Output: [6, 5, 3, 2, 1, 7, 8]

# List Repetition: repeating a list using '*'
repeated_list = [0] * 5
print("Repeated list:", repeated_list)  # Output: [0, 0, 0, 0, 0]

# Checking membership using 'in' operator
is_present = 5 in list_of_numbers
print("Is 5 in the list?", is_present)  # Output: True

# Length of the list using len()
print("Length of the list:", len(list_of_numbers))  # Output: 5

# 5. Nested Lists
# A nested list is a list that contains other lists as elements.

nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested list:", nested_list)

# Accessing elements in a nested list
print("First nested list:", nested_list[0])  # Output: [1, 2]
print("Element from nested list:", nested_list[1][0])  # Output: 3 (second list, first element)

# 6. List Comprehension
# List comprehension provides a concise way to create lists by performing operations on each element.

# Syntax: [expression for item in iterable if condition]

squared_numbers = [x ** 2 for x in range(5)]  # Squares of numbers from 0 to 4
print("Squared numbers:", squared_numbers)  # Output: [0, 1, 4, 9, 16]

# Using condition in list comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# 7. List Mutability
# Lists are mutable, meaning their elements can be changed after creation.

# Modify an element in a list
list_of_numbers[0] = 10
print("After modification:", list_of_numbers)  # Output: [10, 5, 3, 2, 1]

# 8. Nested List Iteration
# You can loop through nested lists using nested loops.

for inner_list in nested_list:
    for item in inner_list:
        print(item, end=" ")  # Output: 1 2 3 4 5 6

# 9. Important Points for Exams
"""
>>> teas[1:1]
note it is empty as 1 is included but 1 is also excluded
[]

- Lists are ordered collections of elements and can contain any data type.
- Lists are mutable, meaning their contents can be modified.
- Lists support various methods like append(), pop(), remove(), sort(), reverse(), etc.
- List comprehension is a concise way to generate or modify lists.
- Nested lists can be used to create lists within lists and can be accessed using multiple indices.
- List operations include concatenation, repetition, and checking for membership.
- Lists can be indexed, sliced, and modified directly.
"""

# End of List Learning
