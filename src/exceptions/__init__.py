def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        raise  # Re-raise the ZeroDivisionError to propagate it
    return result

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
