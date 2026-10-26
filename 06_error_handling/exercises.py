# Error Handling Exercises

# ============================================
# Exercise 1: Safe Division
# Ask the user for two numbers.
# Print the result of dividing the first by the second.
# Handle two errors:
#   - If they don't enter a number → "Please enter a valid number!"
#   - If they divide by zero → "Cannot divide by zero!"
# ============================================

# # Write your code below:

# try:
#     num1 = float(input("1st digit: "))
#     num2 = float(input("2nd digit: "))
#     result = num1/num2
#     print(result)
# except ValueError as e:
#     print(f"Please Enter a valid number! Error is {e}")

# except ZeroDivisionError as e:
#     print(f"Cannot divide by zero! Error is {e}")


# ============================================
# Exercise 2: Safe List Access
# Given this list:
items = ["apple", "banana", "cherry"]
# Ask the user for an index number.
# Print the item at that index.
# Handle errors:
#   - Invalid number → "Please enter a valid number!"
#   - Index out of range → "Index out of range! Use 0-2."
# ============================================

# Write your code below:

# try:
#     index = int(input("Enter an index: "))
#     print(items[index])
# except ValueError:
#     print("Please enter a valid number!")
# except IndexError:
#     print("Index out of range! Use 0-2")

# ============================================
# Exercise 3: Safe File Reader
# Ask the user for a filename.
# Try to open and print the file contents.
# If the file doesn't exist, print:
#   "File not found: <filename>"
# ============================================

# Write your code below:


# try: 
#     filename = input("What filename?: ")
#     with open(filename, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError: 
#     print(f"File not found: {filename}")

# ============================================
# Exercise 4: Number Collector
# Keep asking the user to enter numbers.
# If they enter something that's not a number,
# print "Skipping invalid input" and continue.
# When they type "done", stop and print the sum.
# Hint: use try/except inside a while loop
# ============================================

# Write your code below:

# total = 0
# while True:
#     try:
#         num = input("Enter a number: ")
#         if num == "done":
#             break
#         total += int(num)
#     except ValueError:
#         print("Skipping invalid input")
# print(total)

# ============================================
# Exercise 5: Age Validator
# Create a function called "get_age" that:
#   - Takes an age as a parameter
#   - Raises ValueError if age < 0 or age > 150
#   - Returns the age if valid
# Then ask the user for their age and use try/except
# to catch the error.
# ============================================

# Write your code below:

# def get_age(age):
#     if age < 0 or age > 150:
#         raise ValueError("Age must be between 0 and 150")
#     return age

# try:
#     age = int(input("Enter your age: "))
#     age = get_age(age)
#     print(f"your age is: {age}")

# except ValueError as e:
#     print(e)

# ============================================
# Exercise 6: Safe Calculator
# Create a calculator that:
#   - Asks for two numbers and an operation (+, -, *, /)
#   - Handles invalid numbers (ValueError)
#   - Handles division by zero (ZeroDivisionError)
#   - Handles invalid operation (print "Unknown operation")
#   - Keeps running until user types "quit"
# ============================================

# Write your code below:

while True:
    try:
        op = input("Enter operation: ")
        if op == "quit":
            break
        num1 = int(input("Enter first digit: "))
        num2 = int(input("Enter second digit: "))
        if op == "+":
            total = num1 + num2
        elif op == "-":
            total = num1 - num2
        elif op == "*":
            total = num1 * num2
        elif op == "/":
            total = num1 / num2
        else:
            print("Unknown operation")
            continue

        print(total)

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)