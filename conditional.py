
# 1. IF STATEMENT
# Condition True ho to code run hota hai

age = 20

if age >= 18:
    print("You are an adult")


# 2. IF ELSE STATEMENT
# True ho to if, warna else run hota hai

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")


# 3. IF ELIF ELSE STATEMENT
# Multiple conditions check karne ke liye

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Need more practice")


# 4. NESTED IF
# Ek if ke andar doosra if

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("You are underage")
