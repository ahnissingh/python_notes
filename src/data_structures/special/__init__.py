from collections import namedtuple
from collections import deque
from collections import Counter
from collections import UserDict

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"X: {p.x}, Y: {p.y}")  # Output: X: 10, Y: 20

# Access elements by index
print(p[0])  # Output: 10
# 2 Deque doubly ended queue
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)  # Output: deque([0, 1, 2, 3, 4])
dq.pop()  # Removes 4
dq.popleft()  # Removes 0
print(dq)  # Output: deque([0, 1, 2, 3, 4])

# 3  Counter A dictionary subclass for counting hashable objects.
# Count occurrences in a list
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
color_count = Counter(colors)
# Output: Counter({'blue': 3, 'red': 2, 'green': 1})
print(color_count)
print(color_count.most_common(1))  # Output: [('blue', 3)]

# 4 UserDict
# What it is: A wrapper around dictionary objects,
# allowing customization by subclassing.
# key value pair leta hai __setitem__ ovveride karne me
# Tum apni marji pe key value set karva sktw
class MyDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("Only String Keys are allowed")
        super().__setitem__(key, value)

d = MyDict()
d['key'] = 'value'
print(d)
# d[1] error
