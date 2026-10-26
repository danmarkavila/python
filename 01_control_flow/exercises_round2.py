# Control Flow Exercises - Round 2
# These are slightly harder to sharpen your skills.

# ============================================
# Exercise 1: FizzBuzz (classic!)
# Print numbers from 1 to 30.
# If divisible by 3, print "Fizz" instead.
# If divisible by 5, print "Buzz" instead.
# If divisible by both 3 and 5, print "FizzBuzz".
# Otherwise, print the number.
# Example: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz...
# ============================================

# Write your code below:

for i in range(1, 31):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)

# ============================================
# Exercise 2: Countdown Timer
# Ask the user for a starting number.
# Count down from that number to 1.
# At the end, print "Go!"
# Example: if user enters 5 → 5, 4, 3, 2, 1, Go!
# ============================================

# Write your code below:

number = int(input("Please enter your desired number: "))
for i in range(number, 0, -1):
    print(i)
print("Go!")


# ============================================
# Exercise 3: Password Checker
# The correct password is "python123".
# Give the user 3 attempts to guess it.
# If they get it right, print "Access granted!"
# If they use all 3 attempts, print "Account locked."
# Hint: use a for loop with range(3) and break
# ============================================

# Write your code below:

for i in range(3):
    pw = input("Enter your password: ")
    if pw == "mypass123":
        print("Access Granted!")
        break
else:
    print("Account Locked!")



# ============================================
# Exercise 4: Find the Largest
# Ask the user to enter 5 numbers (one at a time).
# At the end, print the largest number.
# Hint: keep track of the largest so far in a variable
# ============================================

# Write your code below:

for i in range(5):
    number = int(input("Enter your number: "))
    if i == 0:
        largest = number
    elif number > largest:
        largest = number
print(f"The largest number is {largest}")



# ============================================
# Exercise 5: Number Pyramid
# Print this pattern using nested loops:
# *
# **
# ***
# ****
# *****
# Hint: the outer loop controls rows,
# the inner loop controls how many * per row
# ============================================

# Write your code below:

for i in range(1, 10):
    for j in range(i):
        print("*", end="")
    print()


# ============================================
# Exercise 6: Average Calculator
# Ask the user to keep entering numbers.
# When they type 0, stop and print the average.
# Don't include the 0 in the calculation.
# Hint: track both the total and how many numbers
# ============================================

# Write your code below:

count = 0
sum = 0
while True: 

    num = int(input("Please enter a number: "))
    if num == 0:
        break
    sum += num 
    count += 1
average = sum / count
print(f"The average is {average}")