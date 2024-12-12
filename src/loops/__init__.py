"""
Loops in Python

Python provides two types of loops for iteration:
1. **For Loop**
2. **While Loop**

This documentation will cover both, their syntax, usage, and practical applications.
"""

# --- 1. `for` Loop in Python ---
"""
The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It is the most common loop type used in Python because it directly iterates over elements of a sequence.

### Syntax:
    for element in sequence:
        # code block

Where:
- `element` is a variable that holds the value of the current item in the sequence during each iteration.
- `sequence` can be a list, tuple, string, or any other iterable object.

### Examples:

1. **Iterating over a list:**
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # Output:
    # apple
    # banana
    # cherry

2. **Using `range()` to iterate through numbers:**
    range(start, stop, step) - generates a sequence of numbers.

    for i in range(3, 10, 2):
        print(i)

    # Output:
    # 3
    # 5
    # 7
    # 9

3. **Iterating over a string:**
    message = "Python"
    for char in message:
        print(char)

    # Output:
    # P
    # y
    # t
    # h
    # o
    # n
"""

# --- 2. `while` Loop in Python ---
"""
The `while` loop in Python repeatedly executes a block of code as long as the condition is true. It is best used when the number of iterations is not known in advance.

### Syntax:
    while condition:
        # code block

Where:
- `condition` is an expression that returns `True` or `False`. The loop continues as long as this condition is `True`.

### Example:

1. **Simple while loop to print numbers from 1 to 5:**
    counter = 1
    while counter <= 5:
        print(counter)
        counter += 1

    # Output:
    # 1
    # 2
    # 3
    # 4
    # 5

2. **Infinite loop (use with caution):**
    while True:
        print("This loop runs forever.")
        break  # Use a break statement to exit

    # Output:
    # This loop runs forever.
"""

# --- 3. `for` Loop with Nested Iteration ---
"""
A `for` loop can also be nested inside another `for` loop. This is useful when dealing with multi-dimensional data (e.g., lists of lists, matrices).

### Example: Nested loop to iterate through a 2D list:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
"""

# --- 4. `for` Loop with `else` Clause ---
"""
In Python, `for` loops can have an optional `else` block. The `else` block executes when the loop finishes normally (i.e., no `break` is encountered).

### Example:
    for i in range(3):
        print(i)
    else:
        print("Loop finished.")

    # Output:
    # 0
    # 1
    # 2
    # Loop finished.
"""

# --- 5. `break` and `continue` in Loops ---
"""
- **`break`**: Exits the loop entirely, even if the loop condition is still true.
- **`continue`**: Skips the current iteration and moves to the next iteration of the loop.

### Example using `break`:
    for i in range(5):
        if i == 3:
            break
        print(i)

    # Output:
    # 0
    # 1
    # 2

### Example using `continue`:
    for i in range(5):
        if i == 2:
            continue
        print(i)

    # Output:
    # 0
    # 1
    # 3
    # 4
"""

# --- 6. Practical Use Cases / Exam Questions ---

# **Summing Numbers using a Loop**
"""
A common exam question is summing the elements of a list. Here's how you can do that using a `for` loop:

### Example - Sum of numbers in a list:
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Sum:", total)

# Output:
# Sum: 15
"""

# **Reversing a Number**
"""
Reversing a number can be done using a loop. Here's how you can reverse a number without converting it to a string:
The // symbol in Python is used for integer division, 
### Example - Reverse a number:
num = 12345
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num = num // 10
print("Reversed number:", reverse)

# Output:
# Reversed number: 54321
"""

# **Palindrome Check using a Loop**
"""
To check if a number or string is a palindrome, we can reverse the string/number and compare it to the original.

### Example - Check if a number is palindrome:
num = 121
original = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num = num // 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

# Output:
# 121 is a palindrome.
"""

# **Fibonacci Series using a Loop**
"""
The Fibonacci series is a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1. Here's how to generate the Fibonacci series using a `for` loop.

### Example - Fibonacci series up to n terms:
n_terms = 10
a, b = 0, 1
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b

# Output:
# 0 1 1 2 3 5 8 13 21 34
"""

# **Factorial of a Number using a Loop**
"""
To calculate the factorial of a number, you multiply the number by all positive integers less than it.

### Example - Factorial of a number:
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)

# Output:
# Factorial: 120

# Function to check if a string is a palindrome
def is_palindrome_loop(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    length = len(string)
    
    # Compare characters from the beginning and end
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

# Example Usage
word = "Hello"
if is_palindrome_loop

"""



# --- Conclusion ---
"""
This documentation covers the fundamental loop structures in Python, the `for` and `while` loops, their syntaxes, and their use in solving practical problems. 
The provided examples also cover common exam questions such as summing numbers, reversing a number, checking for palindromes, generating Fibonacci sequences, and calculating factorials. 
Understanding these loop structures will help you in writing efficient Python code and solving real-world problems.
"""

