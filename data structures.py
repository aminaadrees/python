# 1. LIST
# List is ordered and changeable

fruits = ["Apple", "Banana", "Mango"]
print("List:", fruits)

print("First fruit:", fruits[0])

fruits.append("Orange")
print("After adding:", fruits)

fruits.remove("Banana")
print("After removing:", fruits)


# 2. TUPLE
# Tuple is ordered but cannot be changed

colors = ("Red", "Green", "Blue")
print("Tuple:", colors)

print("First color:", colors[0])


# 3. SET
# Set stores unique values; order is not guaranteed

numbers = {1, 2, 3, 2, 1}
print("Set:", numbers)

numbers.add(4)
print("After adding:", numbers)

numbers.remove(2)
print("After removing:", numbers)


# 4. DICTIONARY
# Dictionary stores data as key-value pairs

student = {
    "name": "Ahmad",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

print("Student name:", student["name"])

student["age"] = 21
print("Updated age:", student["age"])

student["city"] = "Lahore"
print("After adding city:", student)

print("All keys:", student.keys())
print("All values:", student.values())

print("Data structures practice completed!")