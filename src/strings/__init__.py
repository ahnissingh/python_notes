"""
Python String Learning - Comprehensive Guide

This Python file covers all essential concepts related to strings.
It includes string creation, indexing, slicing, methods, string formatting, and more.
This is a one-stop guide for understanding strings in Python.

Key Topics:
- String Creation
- Indexing and Slicing
- String Methods
- String Formatting
- Escape Characters
- Multiline Strings
- Immutability of Strings
- String Concatenation and Repetition
"""

# 1. String Creation
# A string can be created using either single quotes, double quotes, or triple quotes.
string1 = 'Hello, World!'  # Single quote string
string2 = "Python Programming"  # Double quote string
string3 = '''This is a
multiline string.'''  # Triple quotes for multi-line strings

# 2. String Indexing
# Strings are indexed, meaning each character in a string has a position (starting from 0).
# Negative indexing starts from -1 (last character).
print("Indexing in string:", string1[0])  # Output: H (first character)
print("Negative Indexing:", string1[-1])  # Output: ! (last character)

# 3. String Slicing
# String slicing allows you to extract parts of a string by specifying the start, stop, and step.
# Syntax: string[start:end:step]

substring = string1[0:5]  # Extracts characters from index 0 to 4
print("String slicing (0:5):", substring)  # Output: Hello

# Using step value to skip characters
substring_with_step = string2[::2]  # Skips every second character
print("String slicing with step:", substring_with_step)  # Output: Pto rgamn

# 4. String Methods
# Python provides various built-in methods for working with strings.

# Convert string to lowercase and uppercase
lowercase_string = string2.lower()
uppercase_string = string2.upper()
print("Lowercase:", lowercase_string)  # Output: python programming
print("Uppercase:", uppercase_string)  # Output: PYTHON PROGRAMMING

# Check if a string contains a certain word
contains_word = "Python" in string2
print("Contains 'Python':", contains_word)  # Output: True

# Find the position of a substring
position = string2.find("Programming")
print("Position of 'Programming':", position)  # Output: 7

# Replace part of the string
replaced_string = string2.replace("Python", "Java")
print("Replaced string:", replaced_string)  # Output: Java Programming

# 5. String Formatting
# Python allows various ways to format strings.

# Using f-strings (Python 3.6+)
name = "Ahnis"
age = 21
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Using the format() method
formatted_string_method = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string_method)

# 6. Escape Characters
# Escape characters are used to insert special characters like newlines, tabs, quotes, etc.
escaped_string = "This is a string with a newline\nand this is the next line."
print("Escape character example:", escaped_string)

# 7. Multiline Strings
# Triple quotes can be used to create strings that span multiple lines.
multiline_string = '''This is the first line.
This is the second line.'''
print("Multiline string:\n", multiline_string)

# 8. Immutability of Strings
# Strings in Python are immutable, meaning once created, they cannot be changed.
# Attempting to modify a string directly will result in an error.

# This will cause an error:
# string1[0] = 'h'  # TypeError: 'str' object does not support item assignment

# Instead, you can create a new string:
modified_string = "h" + string1[1:]
print("Modified string:", modified_string)

# 9. String Concatenation and Repetition
# Concatenation combines strings using the '+' operator.
# Repetition repeats a string using the '*' operator.

concatenated_string = string1 + " " + string2
repeated_string = "Hello " * 3
print("Concatenated string:", concatenated_string)
print("Repeated string:", repeated_string)

# 10. Common String Operations and Methods
# - len(): Returns the length of a string
# - strip(): Removes leading and trailing whitespaces
# - split(): Splits a string into a list of substrings
# - join(): Joins elements of a list into a single string

string_with_spaces = "   Hello Python   "
print("Length of string:", len(string1))  # Output: 13
print("String after strip:", string_with_spaces.strip())  # Output: 'Hello Python'

# Split string into list
words = string2.split()
print("Words in string:", words)  # Output: ['Python', 'Programming']

# Join list into a string
joined_string = "-".join(words)
print("Joined string:", joined_string)  # Output: Python-Programming


chai = 'he said \"Masala Chai is Awesome \"'
print(chai)

chai2 = r'he said "Masala Chai is Awesome "'
print(chai)

# path = "c:\user\pwd" is issue
path = r"c:\user\pwd"
print(path)

"""
Important Points for Exams:
- Understand string indexing, slicing, and how to manipulate strings.
- Learn the various built-in string methods like lower(), upper(), find(), replace(), etc.
- Practice using f-strings and the format() method for string formatting.
- Be aware of escape characters and how to use them for special symbols.
- Memorize the key methods like strip(), split(), join(), etc.
- Understand string immutability in Python.
"""

# End of String Learning
