class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand Must be Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operand Must be Vector")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x, self.y})"


# Creating instances of the Vector class
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using overloaded + operator
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# Using overloaded - operator
v4 = v1 - v2
print(v4)  # Output: Vector(-2, -2)

# Using overloaded == operator
print(v1 == Vector(2, 3))  # Output: True
print(v1 == v2)  # Output: False
