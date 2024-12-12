"""
This script demonstrates various Python data types with detailed explanations and usage examples.

Data types covered:
- Integer
- Floating-point
- String
- Boolean
- List
- Tuple
- Dictionary
- Set
"""


def demonstrate_integer():
    """
    Demonstrates the use of integer data type.

    Integer values are whole numbers without a fractional component.

    Returns:
    str: A description of the integer value.
    """
    integer = 42
    return f"Integer value: {integer}"


def demonstrate_float():
    """
    Demonstrates the use of floating-point data type.

    Floating-point values represent real numbers and are used for numbers with a fractional part.

    Returns:
    str: A description of the floating-point value.
    """
    floating_point = 3.14159
    return f"Floating-point value: {floating_point}"


def demonstrate_string():
    """
    Demonstrates the use of string data type.

    String values represent sequences of characters enclosed in quotes. They are used for text.

    Returns:
    str: A description of the string value.
    """
    string = "Hello, Python!"
    return f"String value: {string}"


def demonstrate_boolean():
    """
    Demonstrates the use of boolean data type.

    Boolean values represent truth values, either True or False.

    Returns:
    str: A description of the boolean value.
    """
    boolean = True
    return f"Boolean value: {boolean}"


def demonstrate_list():
    """
    Demonstrates the use of list data type.

    Lists are ordered collections of items that can be of different data types. Lists are mutable.

    Returns:
    str: A description of the list value.
    """
    list_example = [1, 2.5, "three", True]
    return f"List value: {list_example}"


def demonstrate_tuple():
    """
    Demonstrates the use of tuple data type.

    Tuples are ordered collections of items similar to lists but are immutable. They can hold different data types.

    Returns:
    str: A description of the tuple value.
    """
    tuple_example = (1, 2.5, "three", True)
    return f"Tuple value: {tuple_example}"


def demonstrate_dictionary():
    """
    Demonstrates the use of dictionary data type.

    Dictionaries are unordered collections of key-value pairs. Keys must be unique, and values can be of any data type.

    Returns:
    str: A description of the dictionary value.
    """
    dictionary_example = {"one": 1, "two": 2, "three": 3}
    print(type(dictionary_example.keys()))
    return f"Dictionary value: {dictionary_example}"


def demonstrate_set():
    """
    Demonstrates the use of set data type.

    Sets are unordered collections of unique items. They do not allow duplicate values.

    Returns:
    str: A description of the set value.
    """
    set_example = {1, 2, 3}
    return f"Set value: {set_example}"


# Example usage
if __name__ == "__main__":
    print(demonstrate_integer())
    print(demonstrate_float())
    print(demonstrate_string())
    print(demonstrate_boolean())
    print(demonstrate_list())
    print(demonstrate_tuple())
    print(demonstrate_dictionary())
    print(demonstrate_set())
