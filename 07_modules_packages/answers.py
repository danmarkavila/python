# Modules and Packages Answers — try solving them yourself first!

# Exercise 1: Math Module
import math

print(math.sqrt(144))
print(f"{math.pi:.2f}")
print(math.pow(2, 10))

# Exercise 2: Random Module
import random

colors = ["red", "blue", "green", "yellow", "purple"]
print(random.randint(1, 100))
print(random.choice(colors))
random.shuffle(colors)
print(colors)

# Exercise 3: Create Your Own Module
import my_tools

print(my_tools.square(5))
print(my_tools.is_positive(-3))
print(my_tools.APP_NAME)

# Exercise 4: Selective Import
from math import sqrt, pi

print(sqrt(256))
print(pi)

# Exercise 5: Directory Lister
import os

print(os.getcwd())
print(os.listdir("."))
print(os.path.exists("my_tools.py"))

# Exercise 6: Password Generator
import random
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

print(generate_password())
print(generate_password(12))
print(generate_password(16))
