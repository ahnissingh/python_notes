# Functional Programming Tools in Python

# ---------------------- Built-in Functions ----------------------

# 1. **map()**
# Applies a function to each item in an iterable and returns a map object (an iterator).
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)

print("Squared Numbers:", list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 2. **filter()**
# Filters elements from an iterable based on a condition provided by a function.
# Syntax: filter(function, iterable)
even_number_func = lambda x: x % 2 == 0
even_numbers = filter(even_number_func, numbers)
print("Even Numbers:", list(even_numbers))  # Output: [2, 4]

# 3. **sorted()**
# Returns a sorted list from the iterable.
# Syntax: sorted(iterable, key=None, reverse=False)

unsorted_numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(unsorted_numbers)
print("Sorted Numbers:", sorted_numbers)  # Output: [1, 2, 5, 7, 9]

# 4. **any()**
# Returns True if any element in the iterable evaluates to True, otherwise False.
# Syntax: any(iterable)

some_numbers = [0, 1, 0, 3, 0]
print("Any Non-zero Numbers:", any(some_numbers))  # Output: True

# 5. **all()**
# Returns True if all elements in the iterable evaluate to True, otherwise False.
# Syntax: all(iterable)

all_non_zero = [1, 2, 3, 4]
print("All Non-zero Numbers:", all(all_non_zero))  # Output: True

# 6. **zip()**
# Combines multiple iterables element by element into tuples.
# Syntax: zip(iterable1, iterable2, ...)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)
print("Zipped List:", list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# 7. **lambda()**
# A way to create anonymous (inline) functions.
# Syntax: lambda arguments: expression

# Example with map and filter:
cubed_numbers = map(lambda x: x ** 3, numbers)
print("Cubed Numbers:", list(cubed_numbers))  # Output: [1, 8, 27, 64, 125]

# ---------------------- Functions from functools ----------------------

# Import functools functions
from functools import reduce, partial

# 1. **reduce()**
# Applies a binary function cumulatively to the items of an iterable, reducing it to a single value.
# Syntax: reduce(function, iterable[, initializer])

product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)  # Output: 120


# 2. **partial()**
# Creates a new function by fixing some of the arguments of an existing function.
# Syntax: partial(func, *args, **kwargs)

def multiply(x, y):
    return x * y


# Create a new function that always multiplies by 2
double = partial(multiply, 2)

# Now, we can call `double` with just one argument
print("Double of 5:", double(5))  # Output: 10

# ---------------------- Additional Functional Programming Techniques ----------------------

# 8. **List Comprehension**
# A concise way to create lists based on existing iterables and conditions.
squared_numbers_comprehension = [x ** 2 for x in numbers]
print("Squared Numbers (Comprehension):", squared_numbers_comprehension)  # Output: [1, 4, 9, 16, 25]
