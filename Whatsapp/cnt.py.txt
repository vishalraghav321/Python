x = 15
fruits = ["apple", "banana", "cherry"]  # list (mutable)
if x > 20:
    print("x is greater than 20")
elif x == 15:
    print("x is exactly 15")
else:
    print("x is less than 20")

print("\nFor Loop Example:")
for fruit in fruits:
    print(fruit)

print("\nWhile Loop Example:")
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

print()
