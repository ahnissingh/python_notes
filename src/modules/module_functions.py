import importlib
import sys
import math

# 1. importlib.import_module()
# Use case: Dynamically import a module based on a string (e.g., user input)
print("1. importlib.import_module()")
math_module = importlib.import_module('math')  # Dynamically import math module
result = math_module.sqrt(16)  # Use the sqrt function from math module
print(f"Square root of 16: {result}\n")

# 2. importlib.reload()
# Use case: Reload a module after changes (without restarting the interpreter)
print("2. importlib.reload()")
importlib.reload(math_module)  # Reload the math module to apply any changes
print("Math module reloaded successfully!\n")

# 3. dir()
# Use case: Inspect the contents (attributes and functions) of a module
print("3. dir()")
attributes = dir(math_module)  # List all attributes and functions in the math module
print("Attributes in math module:")
for attr in attributes:
    print(attr)
print()  # Newline for readability

# 4. __import__()
# Use case: Import a module dynamically (alternative to importlib)
print("4. __import__()")
my_module = __import__('math')  # Dynamically import the math module
print(f"Square root of 16 using __import__: {my_module.sqrt(16)}\n")

# 5. globals() vs locals()
# Use case: Compare global and local symbol tables
print("5. globals() vs locals()")
global_vars = globals()  # Get global symbol table
local_vars = locals()  # Get local symbol table
print("Global variables:")
print(global_vars.keys())  # List all global variable names
print("Local variables:")
print(local_vars.keys())  # List all local variable names
print()  # Newline for readability

# 6. sys.modules
# Use case: Inspect sys.modules for cached/imported modules
print("6. sys.modules")
import sys
import math  # Import math to make sure it is in sys.modules

cached_modules = sys.modules  # Retrieve the cached modules in sys
print("Modules loaded in sys.modules:")
for module_name in cached_modules:
    print(module_name)
print(f"\nThe math module is loaded: {'math' in sys.modules}\n")

# 7. help()
# Use case: Display documentation for a module or function
print("7. help()")
help(math)  # Display documentation for the math module
print()  # Newline for readability

# Additional Feature: Dynamically load and execute a function
# Use case: Execute a function dynamically based on input
print("8. Dynamically loading a function from a module")
function_name = 'sqrt'
if hasattr(math_module, function_name):
    func = getattr(math_module, function_name)
    print(f"Result of {function_name}(16): {func(16)}")
else:
    print(f"Function {function_name} not found in {math_module.__name__} module.\n")

print("9 Type of module")
print(type(math_module))
