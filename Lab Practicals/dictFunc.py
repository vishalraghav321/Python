# 5C: Dictionary basic operations

student = {"name": "Rahul", "roll_no": 101, "course": "MCA"}

# Accessing values
print("Name :", student["name"])
print("Roll No :", student.get("roll_no"))

# Adding new key-value pair
student["marks"] = 88
print("After adding marks :", student)

# Updating value
student["course"] = "MCA 2nd Year"
print("After updating course :", student)

# Deleting key-value pair
del student["marks"]
print("After deleting marks :", student)

# Dictionary functions
print("Keys :", student.keys())
print("Values :", student.values())
print("Items :", student.items())
