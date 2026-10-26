# Round 2 Answers — try solving them yourself first!

# Exercise 1: FizzBuzz
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 2: Countdown Timer
start = int(input("Enter a starting number: "))
for i in range(start, 0, -1):
    print(i)
print("Go!")

# Exercise 3: Password Checker
for i in range(3):
    guess = input("Enter password: ")
    if guess == "python123":
        print("Access granted!")
        break
else:
    print("Account locked.")

# Exercise 4: Find the Largest
largest = int(input("Enter number 1: "))
for i in range(2, 6):
    num = int(input(f"Enter number {i}: "))
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")

# Exercise 5: Number Pyramid
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Exercise 6: Average Calculator
total = 0
count = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1
if count > 0:
    print(f"Average: {total / count}")
else:
    print("No numbers entered.")
