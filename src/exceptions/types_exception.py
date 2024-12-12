def zero_division_error_example():
    try:
        x = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

def type_error_example():
    try:
        x = "hello" + 5  # This will raise a TypeError (can't concatenate string and integer)
    except TypeError as e:
        print(f"TypeError: {e}")

def value_error_example():
    try:
        x = int("hello")  # This will raise a ValueError (invalid literal for int())
    except ValueError as e:
        print(f"ValueError: {e}")

def index_error_example():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # This will raise an IndexError (index out of range)
    except IndexError as e:
        print(f"IndexError: {e}")

def key_error_example():
    try:
        my_dict = {'name': 'John', 'age': 30}
        print(my_dict['address'])  # This will raise a KeyError (key not found)
    except KeyError as e:
        print(f"KeyError: {e}")

def memory_error_example():
    try:
        # Simulating MemoryError by trying to allocate too much memory
        x = [1] * (10**10)  # This will likely raise a MemoryError (depending on system limits)
    except MemoryError as e:
        print(f"MemoryError: {e}")

def attribute_error_example():
    try:
        x = 10
        x.append(5)  # This will raise an AttributeError (int object has no attribute 'append')
    except AttributeError as e:
        print(f"AttributeError: {e}")

def import_error_example():
    try:
        import non_existent_module  # This will raise an ImportError
    except ImportError as e:
        print(f"ImportError: {e}")

# def indentation_error_example():
#     try:
#         if True:
#         print("This will raise an IndentationError")  # Incorrect indentation
#     except IndentationError as e:
#         print(f"IndentationError: {e}")

def syntax_error_example():
    try:
        eval('x === x')  # This will raise a SyntaxError (invalid syntax)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")

def os_error_example():
    try:
        import os
        os.remove('non_existent_file.txt')  # This will raise an OSError (file not found)
    except OSError as e:
        print(f"OSError: {e}")

def not_implemented_error_example():
    try:
        raise NotImplementedError("This method is not implemented.")  # Explicitly raising NotImplementedError
    except NotImplementedError as e:
        print(f"NotImplementedError: {e}")

def timeout_error_example():
    try:
        raise TimeoutError("The operation timed out.")  # Explicitly raising TimeoutError
    except TimeoutError as e:
        print(f"TimeoutError: {e}")

def file_not_found_error_example():
    try:
        open('non_existent_file.txt')  # This will raise a FileNotFoundError
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

def unicode_error_example():
    try:
        'a' + b'byte'  # This will raise a UnicodeError (mixing string and bytes)
    except UnicodeError as e:
        print(f"UnicodeError: {e}")

def permission_error_example():
    try:
        open('/root/secret.txt', 'w')  # This may raise a PermissionError (insufficient permissions)
    except PermissionError as e:
        print(f"PermissionError: {e}")

# def unbound_local_error_example():
#     try:
#         def foo():
#             print(x)  # This will raise UnboundLocalError because x is referenced before assignment
#             x = 10
#         foo()
#     except UnboundLocalError as e:
#         print(f"UnboundLocalError: {e}")

def recursion_error_example():
    try:
        def recurse():
            recurse()  # This will raise a RecursionError (maximum recursion depth exceeded)
        recurse()
    except RecursionError as e:
        print(f"RecursionError: {e}")

def floating_point_error_example():
    try:
        import math
        print(math.inf / math.inf)  # This will raise a FloatingPointError (NaN)
    except FloatingPointError as e:
        print(f"FloatingPointError: {e}")



def main():
    zero_division_error_example()
    type_error_example()
    value_error_example()
    index_error_example()
    key_error_example()
    # memory_error_example()
    attribute_error_example()

if __name__ == "__main__":
    main()
