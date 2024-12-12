def square(n):
    return n ** 2


import math


def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference


a, c = circle_stats(3)
print(a, c)


def greet_with_default_params(name="User"):
    return "Hello, " + name + " !"


cube = lambda x: x ** 3


def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)


print(sum_all(1, 2, 3, 4, 5, 6))


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal")


# Agar na use karte limit bhut bari hoti to bada time memory
# consuming hota
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Scopes and closures
"""LEGB Rule (Scope Resolution Order):
Local Scope: Variables defined inside a function or block and accessible only within that function or block.
Enclosing Scope: Variables in the local scope of enclosing functions (nested functions).
Global Scope: Variables defined at the top-level of a module or script, accessible anywhere in the module.
Built-in Scope: Python's built-in names like len, sum, print, etc.
"""

"""
A closure is a function object that "remembers" the variables from its enclosing 
scope even if the scope has finished execution.
 Closures are often used to implement encapsulation 
 and create functions with pre-filled arguments."""


def multiplier(factor):
    def multiply_by(n):
        return n * factor

    return multiply_by


times3 = multiplier(3)
print(times3(10))  # Outputs: 30


def logger(msg):
    def log_function():
        print(f"Log: {msg}")

    return log_function


log_error = logger("An error occurred")
log_error()  # Outputs: Log: An error occurred
