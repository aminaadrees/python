# 1. DECLARING A FUNCTION
# def is used to create a function

def greet():
    print("Hello, welcome to Python!")


# 2. CALLING A FUNCTION
# Function runs when we call its name

greet()
greet()


# 3. FUNCTION WITH PARAMETERS

def greet_person(name):
    print("Hello", name)


greet_person("Ahmad")
greet_person("Ali")


# 4. FUNCTION WITH RETURN

def add(a, b):
    return a + b


result = add(10, 5)
print("Sum:", result)


# 5. LOCAL VARIABLE SCOPE
# A variable created inside a function is local

def show_number():
    number = 100
    print("Inside function:", number)


show_number()


# 6. GLOBAL VARIABLE SCOPE
# A variable created outside a function is global

message = "I am a global variable"

def show_message():
    print(message)


show_message()
print("Outside function:", message)


# 7. LOCAL AND GLOBAL VARIABLES WITH SAME NAME

x = 10

def show_x():
    x = 20
    print("Local x:", x)


show_x()
print("Global x:", x)


print("Functions practice completed!")
