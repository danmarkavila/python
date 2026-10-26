# Exercise Answers — try solving them yourself first!

# Exercise 1: Grade Checker
score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Exercise 2: Even or Odd
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} - even")
    else:
        print(f"{i} - odd")

# Exercise 3: Sum Until Negative
total = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total += num
print(f"Total sum: {total}")

# Exercise 4: Skip Multiples of 3
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)

# Exercise 5: Multiplication Table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
