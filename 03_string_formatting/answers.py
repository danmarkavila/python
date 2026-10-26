# String Formatting Answers — try solving them yourself first!

# Exercise 1: Personal Info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")
print(f"In 10 years, you will be {age + 10}.")

# Exercise 2: Receipt Formatter
item = "Widget"
price = 49.999
quantity = 3
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity:.2f}")

# Exercise 3: Number Formatter
big_number = 1234567890
print(f"{big_number:,}")
print(f"{big_number:,.2f}")

# Exercise 4: Score Display
scores = [0.95, 0.8, 0.673, 1.0]
for i in range(len(scores)):
    print(f"Score {i + 1}: {scores[i]:.0%}")

# Exercise 5: Table Formatter
print(f"{'Name':<10} | {'Age':>3} | {'City'}")
print(f"{'Alice':<10} | {30:>3} | {'New York'}")
print(f"{'Bob':<10} | {25:>3} | {'London'}")
print(f"{'Charlie':<10} | {35:>3} | {'Tokyo'}")

# Exercise 6: Multiline Bio
name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")
print(f"""
====================
Name:  {name}
Age:   {age}
Hobby: {hobby}
====================""")
