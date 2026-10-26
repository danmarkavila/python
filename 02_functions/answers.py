# Functions Answers — try solving them yourself first!

# Exercise 1: Simple Greeting
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# Exercise 2: Add Two Numbers
def add(a, b):
    return a + b

print(add(3, 5))
print(add(10, 20))

# Exercise 3: Even or Odd Function
def is_even(num):
    return num % 2 == 0

print(is_even(4))    # True
print(is_even(7))    # False

# Exercise 4: Max of Three
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(max_of_three(3, 9, 5))    # 9
print(max_of_three(10, 2, 7))   # 10

# Exercise 5: Calculator
def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

print(calculate(10, 5, "add"))        # 15
print(calculate(10, 5, "subtract"))   # 5
print(calculate(10, 5, "multiply"))   # 50
print(calculate(10, 5, "divide"))     # 2.0

# Exercise 6: Greeting with Default
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()          # Welcome, Guest!
welcome("Alice")   # Welcome, Alice!
