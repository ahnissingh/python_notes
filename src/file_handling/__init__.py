"""
Mode	Description
'r'	Read (default mode) - Error if file doesn’t exist.
'w'	Write - Creates a file or overwrites it.
'a'	Append - Adds data to the end of the file.
'x'	Create - Creates a new file, error if file exists.
'b'	Binary mode (add to any of the above).
't'	Text mode (default, add to any of the above).

rwa xbt
"""
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Prints all content

with open('example.txt', 'r') as file:
    print('using readline()')
    print(file.readline(), end='')
    print(file.readline(), end='')

with open('example.txt') as file:
    print('using readlines() function')
    lines = file.readlines()
    for line in lines:
        print(line, end='')
"""
Comparison Table:
Method	     Returns	  Reads	     Best Use
read()	     Single      string	     Entire file	When you need the whole content as one string
readline()	 Single      string      (one line at a time)	One line at a time	To process files line by line
readlines()	 List of     strings	 Entire file into a list	To work with each line individu
"""
# 2 Write using write
with open('example.txt', 'w') as file:
    file.write('This is a test file')

# 3 Append -> we stil use "write" function but 'a' as Mode
with open('example.txt', 'a') as file:
    file.write('\n Adding more content')

# File management functions
import os

# 1 Exists
print(os.path.exists('example.txt'))  # True/False
# 2 Rename
# os.rename('example.txt', 'new_example.txt')
# 3 Delete
# os.remove('example.txt')
# Exception Handling
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
# Binary File Handling
with open('image.jpg', 'b') as file:
    data = file.read()

with open('copy_image.jpg', 'wb') as file:
    file.write(data)

# Common Exam Questions
# 1 Count Lines
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

with open('example.txt', 'r') as source, open('destination.txt', 'w') as dest:
    dest.write(source.read())
