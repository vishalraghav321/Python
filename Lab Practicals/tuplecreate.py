# 5A: Tuple operations

# Creation of tuple
t = (10, 20, 30, 40, 50)
print("Tuple :", t)

# Access
print("Element at index 2 :", t[2])

# Slicing
print("Slicing t[1:4] :", t[1:4])

# Unpacking
a, b, c, d, e = t
print("Unpacked Values :", a, b, c, d, e)

# Built-in functions
print("Length of tuple :", len(t))
print("Maximum element :", max(t))
print("Minimum element :", min(t))
print("Sum of elements :", sum(t))
