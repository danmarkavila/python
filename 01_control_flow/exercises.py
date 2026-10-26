# Control Flow Exercises
# Try to solve each one before looking at the answers!

# ============================================
# Exercise 1: Grade Checker
# Ask the user for a score (0-100) and print:
#   "A" if score >= 90
#   "B" if score >= 80
#   "C" if score >= 70
#   "D" if score >= 60
#   "F" otherwise
# ============================================

# Write your code below:
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

# ============================================
# Exercise 2: Even or Odd
# Print all numbers from 1 to 20.
# Next to each number, print "even" or "odd".
# Example output: "1 - odd", "2 - even", ...
# ============================================

# Write your code below:

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} - even")
    else:
        print(f"{i} - odd")




# ============================================
# Exercise 3: Sum Until Negative
# Ask the user to keep entering numbers.
# Add them up as they go.
# Stop when they enter a negative number.
# Print the total sum (don't include the negative).
# Hint: use a while loop and break
# ============================================

# Write your code below:

total = 0
while True:
    number = int(input("Enter your number here: "))
    if number < 0:
        break
    total += number
    print(f"total number: {total}")
    

# ============================================
# Exercise 4: Skip Multiples of 3
# Print numbers from 1 to 30, but skip any
# number that is a multiple of 3.
# Hint: use continue and the % operator
# ============================================

# Write your code below:


for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)


# ============================================
# Exercise 5: Multiplication Table
# Print a multiplication table for numbers 1-5.
# Example output:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 5 x 5 = 25
# Hint: use nested for loops
# ============================================

# Write your code below:


for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
