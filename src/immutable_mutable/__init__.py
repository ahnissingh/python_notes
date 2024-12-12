x = 5
id1 = id(x)
print("Current id of x is", id1)
x = x * 2
id2 = id(x)
print("Now id of x is ", id2)
print((id1.__eq__(id2)))
print(id1 == id2)
