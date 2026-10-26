# Comprehension Exercises

# ============================================
# Exercise 1: Double It
# Given this list:
numbers = [3, 7, 2, 9, 1, 5]
# Create a new list with each number doubled
# using a list comprehension.
# Expected: [6, 14, 4, 18, 2, 10]
# ============================================

# Write your code below:

# doubled = [n * 2 for n in numbers]
# print(doubled)

# ============================================
# Exercise 2: Filter Short Words
# Given this list:
words = ["cat", "elephant", "dog", "hippopotamus", "ant", "giraffe"]
# Create a new list with only words that have
# more than 3 letters, using a list comprehension.
# Expected: ['elephant', 'hippopotamus', 'giraffe']
# ============================================

# Write your code below:

# limited = [word for word in words if len(word) > 3]
# print(limited)


# ============================================
# Exercise 3: Pass or Fail
# Given this list of scores:
scores = [85, 42, 73, 91, 38, 67, 55]
# Create a new list that says "pass" if score >= 60,
# "fail" otherwise. Use if/else in a comprehension.
# Expected: ['pass', 'fail', 'pass', 'pass', 'fail', 'pass', 'fail']
# ============================================

# Write your code below:

# checked = ["pass" if i >= 60 else "fail" for i in scores]
# print(checked)

# ============================================
# Exercise 4: Word Lengths Dict
# Given this list:
fruits = ["apple", "banana", "cherry", "kiwi"]
# Create a dictionary where the key is the fruit
# and the value is its length.
# Expected: {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4}
# ============================================

# Write your code below:

# dictionary = {fruit: len(fruit) for fruit in fruits}
# print(dictionary)
# ============================================
# Exercise 5: Unique First Letters
# Given this list:
cities = ["Tokyo", "Toronto", "London", "Lima", "Paris", "Prague"]
# Create a SET of the first letter of each city.
# Expected: {'T', 'L', 'P'}
# ============================================

# Write your code below:

# unique = {city[0] for city in cities}
# print(unique)



# ============================================
# Exercise 6: Celsius to Fahrenheit
# Given these temperatures in Celsius:
celsius = [0, 10, 20, 30, 40]
# Create a new list with each converted to Fahrenheit.
# Formula: (c * 9/5) + 32
# Use a list comprehension.
# Expected: [32.0, 50.0, 68.0, 86.0, 104.0]
# ============================================

# Write your code below:

# fahrenheit = [c * 9/5 + 32 for c in celsius]
# print(fahrenheit)


# ============================================
# Exercise 7: Filter a Dict
# Given this dictionary:
inventory = {"apples": 5, "bananas": 0, "cherries": 12, "dates": 0, "eggs": 3}
# Create a new dict with only items that have
# a quantity greater than 0.
# Expected: {'apples': 5, 'cherries': 12, 'eggs': 3}
# ============================================

# Write your code below:

filtered = {name: value for name, value in inventory.items() if value > 0}
print(filtered)