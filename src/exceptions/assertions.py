# assert condition , message
assert 100 != 10 ** 2, "Assertion true"
age = 25
assert age >= 18, "Age should be at least 18"
print("Age is valid")
""""
For Debugging: Assertions are mainly used as a debugging tool to test conditions that should always be true during development.
Catch Logic Errors Early: They can help identify logic errors early by verifying assumptions about the state of the program.
Simpler than Exception Handling: Using assertions is a simpler way to check conditions than using explicit exception handling for every logical check.
"""

# Practical Use case
def calculate_area(radius):
    assert radius > 0, "Radius must be positive"
    return 3.14 * radius ** 2

