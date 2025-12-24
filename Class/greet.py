def greet():
    print("Hello")

def add(a,b):
    return a+b

def fact(a):
    if(a==0):
        return 1
    return a*fact(a-1)

def fact2(a=5):          #for default case
    if(a==0):
        return 1
    return a*fact(a-1)

def area(l=20, b=5):
    return l*b

def print_squares(nums):
    for n in nums:
        print(n*n)

def employee(name, salary):
    print("Name = ", name, "Salary =", salary)

greet()
print(add(3,4))
print(fact(6))

print(fact2())
print(fact2(4))

print(area())
print(area(35))
print(area(35, 10))

print_squares([1,2,3,4])

employee("Abhishek", 40000)
employee(salary=67000, name="Vaibhav")




