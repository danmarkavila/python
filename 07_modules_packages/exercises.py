# Modules and Packages Exercises

# ============================================
# Exercise 1: Math Module
# Use the math module to:
#   - Print the square root of 144
#   - Print pi rounded to 2 decimal places
#   - Print 2 to the power of 10 using math.pow()
# ============================================

# Write your code below:

# import math

# print(math.sqrt(144))
# print(f"{math.pi:.2f}")
# print(math.pow(2, 10))



# ============================================
# Exercise 2: Random Module
# Use the random module to:
#   - Print a random number between 1 and 100
#   - Pick a random item from this list:
colors = ["red", "blue", "green", "yellow", "purple"]
#   - Shuffle the list and print it
# ============================================

# Write your code below:

# import random

# print(random.randint(1, 100))
# print(random.choice(colors))
# print(random.shuffle(colors))
# print(colors)
# # print(dir(random))
# # help(random)



# ============================================
# Exercise 3: Create Your Own Module
# Create a file called "my_tools.py" in this folder with:
#   - A function "square" that returns a number squared
#   - A function "is_positive" that returns True if number > 0
#   - A variable "APP_NAME" set to "My Python App"
#
# Then import and use all three in this file.
# ============================================

# Write your code below:

# import my_tools

# print(my_tools.square(5))
# print(my_tools.is_positive(-2))
# print(my_tools.APP_NAME)


# ============================================
# Exercise 4: Selective Import
# From the math module, import ONLY sqrt and pi
# (don't import the whole module).
# Print sqrt(256) and pi.
# ============================================

# Write your code below:

# from math import sqrt, pi

# print(sqrt(256))
# print(pi)


# ============================================
# Exercise 5: Directory Lister
# Use the os module to:
#   - Print the current working directory
#   - List all files in the current directory
#   - Check if "my_tools.py" exists and print the result
# ============================================

# # Write your code below:

# import os

# print(os.getcwd())
# print(os.listdir())
# print(os.path.exists("my_tools.py"))
# print(dir(os))


# ============================================
# Exercise 6: Password Generator
# Use random and string modules to create a function
# called "generate_password" that:
#   - Takes a length parameter (default 8)
#   - Returns a random password with letters and digits
#   - Hint: use string.ascii_letters and string.digits
#   - Hint: use random.choice() in a loop
# Generate and print 3 passwords.
# ============================================

# Write your code below:

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password())
print(generate_password())
print(generate_password())