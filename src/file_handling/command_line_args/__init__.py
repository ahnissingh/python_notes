import sys

print(sys.argv)
# List of arguments
# 0th is name of script , argv[1:] are additional

args = sys.argv[1:]
print('Actual args', args)
argc = len(sys.argv)  # Length of arguments
# argc is not explicitly provided in Python.
# Instead, you use len(sys.argv) to calculate the argument count.
print(f"Arguments Count{argc}")
""""
Usage
Common Use Cases

    Passing configuration values.
    Dynamic behavior based on user input from the command line.
    Automating scripts with arguments.

Benefits

    Flexibility to control script behavior without modifying the code.
"""
