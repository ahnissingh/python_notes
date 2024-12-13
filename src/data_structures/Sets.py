# Python Sets Demonstration

# 1. Creating Sets
set1 = {1, 2, 3, 4, 5}  # Using curly braces
set2 = set([4, 5, 6, 7, 8])  # Using the set() constructor
empty_set = set()  # Empty set (Note: {} creates an empty dictionary)

print("Set 1:", set1)
print("Set 2:", set2)
print("Empty Set:", empty_set)

# 2. Properties of Sets
# Sets are unordered, do not allow duplicate values, and are mutable
set_with_duplicates = {1, 2, 2, 3, 4, 4}
print("Set with duplicates removed:", set_with_duplicates)

# 3. Basic Operations
set1.add(6)  # Add a single element
set1.update([7, 8, 9])  # Add multiple elements
print("Set 1 after adding elements:", set1)

set1.remove(9)  # Remove an element (raises KeyError if not found)
set1.discard(10)  # Remove an element (no error if not found)
print("Set 1 after removals:", set1)

# 4. Mathematical Set Operations
print("Union of Set 1 and Set 2:", set1 | set2)  # Union
print("Intersection of Set 1 and Set 2:", set1 & set2)  # Intersection
print("Difference (Set 1 - Set 2):", set1 - set2)  # Difference
print("Symmetric Difference (elements in either but not both):", set1 ^ set2)

# 5. Subset, Superset, and Disjoint Sets
print("Is Set 2 a subset of Set 1?", set2.issubset(set1))
print("Is Set 1 a superset of Set 2?", set1.issuperset(set2))
print("Are Set 1 and Set 2 disjoint?", set1.isdisjoint(set2))  # True if no common elements

# 6. Iterating Over a Set
print("Iterating through Set 1:")
for element in set1:
    print(element, end=" ")
print()

# 7. Set Comprehensions
squared_set = {x**2 for x in range(1, 6)}  # Creating a set of squares
print("Set Comprehension (Squares):", squared_set)

# 8. Copying and Clearing
set_copy = set1.copy()  # Create a shallow copy
set1.clear()  # Clear all elements in a set
print("Set 1 after clearing:", set1)
print("Copied Set:", set_copy)
