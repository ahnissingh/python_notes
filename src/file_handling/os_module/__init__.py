
# os_module_documentation_example.py

# The os module provides a way to interact with the operating system.
# Below are examples of file handling, path operations, environment variable management, and process control.

import os

# ----------------------------
# 1. File Handling (Creation, Deletion, Manipulation)
# ----------------------------

# Get the current working directory
print("Current directory:", os.getcwd())

# List files in the current directory
print("Files in current directory:", os.listdir('.'))

# Create a new directory
os.mkdir('new_folder')
print("New directory created: new_folder")

# Create a new file in the new directory
with open('new_folder/test_file.txt', 'w') as f:
    f.write("Hello from Python!")

# List files in the 'new_folder' directory
print("Files in new_folder:", os.listdir('new_folder'))

# Remove the file and directory
os.remove('new_folder/test_file.txt')
os.rmdir('new_folder')  # Remove 'new_folder'
print("File and directory removed.")


# ----------------------------
# 2. Path Operations (Cross-platform path manipulation)
# ----------------------------

# Joining paths to form a complete path
full_path = os.path.join('folder', 'subfolder', 'file.txt')
print("Full path:", full_path)

# Check if a path exists
print("Does 'file.txt' exist?", os.path.exists('file.txt'))

# Check if it's a file or directory
print("Is 'file.txt' a file?", os.path.isfile('file.txt'))
print("Is 'folder' a directory?", os.path.isdir('folder'))

# Get the absolute path
print("Absolute path of 'file.txt':", os.path.abspath('file.txt'))

# ----------------------------
# 3. Environment Variables
# ----------------------------

# Get an environment variable
user = os.getenv('USER', 'Not Set')  # Get the USER environment variable
print("Current User:", user)

# Set a new environment variable
os.putenv('MY_VAR', 'HelloWorld')  # Set an environment variable
print("MY_VAR:", os.getenv('MY_VAR'))


# ----------------------------
# 4. Process Control (Running system commands)
# ----------------------------

# Running a system command using os.system()
os.system('echo Hello, World!')  # Prints 'Hello, World!' to the console

# Using os.popen() to run a command and capture the output
result = os.popen('echo Hello from Python').read()
print("Output from os.popen():", result)

# ----------------------------
# End of the script
