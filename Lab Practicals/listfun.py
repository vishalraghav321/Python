# Program to perform list functions

numbers = [10, 20, 30, 40]
print("Original list:", numbers)

print("Access element at index 2:", numbers[2])

numbers.append(50)
numbers.insert(1, 15)
print("After adding elements:", numbers)

numbers.remove(30)
del numbers[0]
print("After removing elements:", numbers)

print("Maximum element:", max(numbers))
print("Minimum element:", min(numbers))
