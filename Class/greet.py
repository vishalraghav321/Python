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

def add_all(*nums):                 #variable length parameters
    print(nums)
    return sum(nums)

def student_info(**details):        #variable length keyword parameters
    print("Name =", details["name"])
    print(details)

def func(a,b,*nums,c=10,**details):     #order of passing parameters
    print("a*b*c = ", a*b*c)
    
    print(nums)

# greet()
# print(add(3,4))
# print(fact(6))

# print(fact2())
# print(fact2(4))

# print(area())
# print(area(35))
# print(area(35, 10))

# print_squares([1,2,3,4])

# employee("Abhishek", 40000)
# employee(salary=67000, name="Vaibhav")

# print(add_all(2,3,7,9))

# student_info(name="Amit", roll=12)
# student_info(name="Ajit", roll=11, Class="MCA")



