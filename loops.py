# 1. FOR LOOP
for i in range(1, 6):
    print(i)

# 2. WHILE LOOP
count = 1
while count <= 5:
    print(count)
    count += 1

# 3. BREAK
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 4. CONTINUE
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 5. ELSE WITH LOOP
for i in range(1, 4):
    print(i)
else:
    print("Loop completed")

# 6. BREAK WITH ELSE
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")