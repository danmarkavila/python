# Functions Exercises

# ============================================
# Exercise 1: Simple Greeting
# Create a function called "greet" that takes
# a name and prints "Hello, <name>!"
# Call it 3 times with different names.
# ============================================

# Write your code below:

def greet(name):
    print(f"Hello, {name}!")

greet("Dan")
greet("Mark")
greet("Avila")


# ============================================
# Exercise 2: Add Two Numbers
# Create a function called "add" that takes
# two numbers, and RETURNS their sum.
# Print the result of calling it.
# ============================================

# Write your code below:

def add(x, y):
    return x + y

result = add(5, 4)
print(result)



# ============================================
# Exercise 3: Even or Odd Function
# Create a function called "is_even" that takes
# a number and RETURNS True if even, False if odd.
# Test it with a few numbers.
# Hint: use the % operator
# ============================================

# Write your code below:

def is_even(number):
    return number % 2 == 0

print(is_even(6)) 
print(is_even(5))




# ============================================
# Exercise 4: Max of Three
# Create a function called "max_of_three" that
# takes 3 numbers and RETURNS the largest one.
# Don't use the built-in max() function.
# ============================================

# Write your code below:

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3
    
print(max_of_three(5, 10, 3))









# ============================================
# Exercise 5: Calculator
# Create a function called "calculate" that takes
# 3 parameters: num1, num2, and operation.
# operation can be "add", "subtract", "multiply", "divide"
# Return the result.
# Example: calculate(10, 5, "add") → 15
# ============================================

# Write your code below:

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
print(calculate(10, 5, "add"))

# ============================================
# Exercise 6: Greeting with Default
# Create a function called "welcome" that takes
# a name with a default value of "Guest".
# It should print "Welcome, <name>!"
# Call it with and without an argument.
# ============================================

# Write your code below:

def welcome(name = "Guest"):
    print(f"Welcome, {name}!")

welcome()
welcome("Dan")
