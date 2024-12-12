"""
Python Tuple Learning - Comprehensive Guide

This Python file covers all essential concepts related to tuples.
It includes tuple creation, indexing, methods, operations, immutability, and more.
This is a one-stop guide for understanding tuples in Python.

Key Topics:
- Tuple Creation
- Indexing and Slicing
- Tuple Methods
- Tuple Operations
- Nested Tuples
- Tuple Unpacking
- Tuple Immutability
"""

# 1. Tuple Creation
# A tuple in Python is an ordered, immutable collection of elements. Tuples are created using parentheses ().
empty_tuple = ()  # Empty tuple
tuple_of_numbers = (1, 2, 3, 4, 5)  # Tuple of integers

tuple_of_strings = ("apple", "banana", "cherry")  # Tuple of strings
mixed_tuple = (1, "apple", 3.14, True)  # Mixed data types tuple

# A tuple can also be created without parentheses, using a comma-separated sequence:
tuple_without_parentheses = 1, 2, 3, 4

# Single element tuple needs a trailing comma to distinguish it from a regular parenthesized expression
single_element_tuple = (1,)  # Tuple with one element

# 2. Tuple Indexing and Slicing
# Tuples are indexed starting from 0, and you can access elements using positive or negative indices.
# Negative indexing starts from -1 (last element).
print("First element:", tuple_of_numbers[0])  # Output: 1 (first element)
print("Last element:", tuple_of_numbers[-1])  # Output: 5 (last element)

# Tuple slicing allows extracting parts of a tuple using the syntax tuple[start:end:step].
sub_tuple = tuple_of_numbers[1:4]  # Extracts elements from index 1 to 3 (4 is excluded)
print("Tuple slicing (1:4):", sub_tuple)  # Output: (2, 3, 4)

# Using step to skip elements
sub_tuple_with_step = tuple_of_numbers[::2]  # Skips every second element
print("Tuple slicing with step:", sub_tuple_with_step)  # Output: (1, 3, 5)

# 3. Tuple Methods
# Tuples have only two built-in methods:
# 1) count() - Counts the number of occurrences of an element.
# 2) index() - Finds the index of the first occurrence of an element.
print("Count of 3:", tuple_of_numbers.count(3))  # Output: 1
print("Index of 4:", tuple_of_numbers.index(4))  # Output: 3

# 4. Tuple Operations
# Tuples support various operations such as concatenation, repetition, and more.

# Tuple Concatenation: combining two tuples using '+'
new_tuple = tuple_of_numbers + (6, 7)
print("Concatenated tuple:", new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Tuple Repetition: repeating a tuple using '*'
repeated_tuple = ("A",) * 3
print("Repeated tuple:", repeated_tuple)  # Output: ('A', 'A', 'A')

# Checking membership using 'in' operator
is_present = 3 in tuple_of_numbers
print("Is 3 in the tuple?", is_present)  # Output: True

# Length of the tuple using len()
print("Length of the tuple:", len(tuple_of_numbers))  # Output: 5

# 5. Nested Tuples
# A nested tuple is a tuple that contains other tuples as elements.

nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)

# Accessing elements in a nested tuple
print("First nested tuple:", nested_tuple[0])  # Output: (1, 2)
print("Element from nested tuple:", nested_tuple[1][0])  # Output: 3 (second tuple, first element)

# 6. Tuple Unpacking
# Tuple unpacking allows you to assign tuple elements to variables.

tuple_to_unpack = (10, 20, 30)
a, b, c = tuple_to_unpack  # Unpacking the tuple into variables a, b, and c
print("Unpacked values:", a, b, c)  # Output: 10 20 30

# Unpacking with an asterisk to catch remaining elements:
tuple_with_extra = (1, 2, 3, 4, 5)
first, *rest = tuple_with_extra  # first gets 1, rest gets [2, 3, 4, 5]
print("First element:", first)  # Output: 1
print("Remaining elements:", rest)  # Output: [2, 3, 4, 5]

# 7. Tuple Immutability
# Tuples are immutable, meaning their contents cannot be changed once created.
# Trying to modify an element of a tuple will raise a TypeError.

# Example of immutability:
# try:
#     tuple_of_numbers[0] = 100  # This will raise an error
# except TypeError as e:
#     print(f"Error: {e}")  # Output: 'tuple' object does not support item assignment

# However, if a tuple contains mutable objects like lists, the mutable objects can be modified.
tuple_with_list = ([1, 2], [3, 4])
tuple_with_list[0][0] = 10  # Modifying the list inside the tuple is allowed
print("Modified tuple:", tuple_with_list)  # Output: ([10, 2], [3, 4])

# 8. Important Points for Exams
"""
- Tuples are ordered collections of elements that are immutable.
- A tuple can contain elements of any data type (including mixed data types).
- Tuples support indexing, slicing, and operations like concatenation and repetition.
- Tuples have limited methods: count() and index().
- Tuples can be nested (tuples inside tuples) and accessed using multiple indices.
- Tuple unpacking allows assignment of tuple elements to multiple variables.
- Tuples are immutable, meaning the elements cannot be changed after creation, but if a tuple contains mutable objects, those can be modified.
- Tuples are commonly used for data that shouldn't change (e.g., coordinates, database records).
"""

# End of Tuple Learning
