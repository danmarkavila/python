# Error Handling Answers — try solving them yourself first!

# Exercise 1: Safe Division
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {a / b}")
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Exercise 2: Safe List Access
items = ["apple", "banana", "cherry"]
try:
    index = int(input("Enter an index: "))
    print(items[index])
except ValueError:
    print("Please enter a valid number!")
except IndexError:
    print("Index out of range! Use 0-2.")

# Exercise 3: Safe File Reader
filename = input("Enter a filename: ")
try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"File not found: {filename}")

# Exercise 4: Number Collector
total = 0
while True:
    entry = input("Enter a number (or 'done'): ")
    if entry == "done":
        break
    try:
        total += int(entry)
    except ValueError:
        print("Skipping invalid input")
print(f"Sum: {total}")

# Exercise 5: Age Validator
def get_age(age):
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150!")
    return age

try:
    age = int(input("Enter your age: "))
    age = get_age(age)
    print(f"Your age is {age}")
except ValueError as e:
    print(f"Error: {e}")

# Exercise 6: Safe Calculator
while True:
    entry = input("Enter operation (or 'quit'): ")
    if entry == "quit":
        break
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        if entry == "+":
            print(f"Result: {a + b}")
        elif entry == "-":
            print(f"Result: {a - b}")
        elif entry == "*":
            print(f"Result: {a * b}")
        elif entry == "/":
            print(f"Result: {a / b}")
        else:
            print("Unknown operation")
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
