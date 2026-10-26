# String Formatting Exercises

# ============================================
# Exercise 1: Personal Info
# Ask the user for their name and age.
# Print: "Hello, <name>! You are <age> years old."
# Also print: "In 10 years, you will be <age+10>."
# Use f-strings.
# ============================================

# Write your code below:

name = str(input("What is your name: "))
age = int(input("What is your age:"))
print(f"Hello, {name}! You are {age} years old.")
print(f"In 10 years, you will be {age+10}.")


# ============================================
# Exercise 2: Receipt Formatter
# Given these variables:
item = "Widget"
price = 49.999
quantity = 3
# Print a receipt like this (use f-strings):
# Item: Widget
# Price: $50.00
# Quantity: 3
# Total: $150.00
# Hint: use :.2f for 2 decimal places
# ============================================

# Write your code below:

item = "Widget"
price = 49.999
quantity = 3
receipt = f"""
Item: {item}
Price: ${price:.2f}
Quantity: {quantity}
Total: ${price * quantity:.2f}
"""
print(receipt)




# ============================================
# Exercise 3: Number Formatter
# Given this number:
big_number = 1234567890
# Print it with commas: 1,234,567,890
# Also print it as a float with 2 decimals: 1,234,567,890.00
# ============================================

# Write your code below:

big_number = 1234567890
print(f"{big_number:,}")
print(f"{big_number:,.2f}")


# ============================================
# Exercise 4: Score Display
# Given these scores:
scores = [0.95, 0.8, 0.673, 1.0]
# Print each score as a percentage:
# Score 1: 95%
# Score 2: 80%
# Score 3: 67%
# Score 4: 100%
# Hint: use :.0% in the f-string
# ============================================

# Write your code below:

scores = [0.95, 0.8, 0.673, 1.0]
for i, score in enumerate(scores, 1):
    print(f"Score {i}: {score:.0%}")


# ============================================
# Exercise 5: Table Formatter
# Print this table using alignment formatting:
# Name       | Age | City
# Alice      |  30 | New York
# Bob        |  25 | London
# Charlie    |  35 | Tokyo
# Hint: use <, >, ^ for alignment with a width
# ============================================

# Write your code below:

name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
age1 = 30
age2 = 25
age3 = 35
city1 = "New York"
city2 = "London"
city3 = "Tokyo"

print(f"{name1:<10}|{age1:^5}|{city1:<10}")
print(f"{name2:<10}|{age2:^5}|{city2:<10}")
print(f"{name3:<10}|{age3:^5}|{city3:<10}")

people = [("Alice", 30, "New York"), ("Bob", 25, "London"), ("Charlie", 35, "Tokyo")]
for name, age, city in people:
    print(f"{name:<10}|{age:^5}|{city:<10}")

# ============================================
# Exercise 6: Multiline Bio
# Ask the user for: name, age, hobby
# Print a bio card using a multiline f-string:
# ====================
# Name:  <name>
# Age:   <age>
# Hobby: <hobby>
# ====================
# ============================================

# Write your code below:

name = input("What is your name?")
age = int(input("What is your age?"))
hobby = input("What is your hobby?")

bio = f"""
Name: {name}
Age: {age}
Hobby: {hobby}
"""
print(bio)