# Comprehension Answers — try solving them yourself first!

# Exercise 1: Double It
numbers = [3, 7, 2, 9, 1, 5]
doubled = [n * 2 for n in numbers]
print(doubled)

# Exercise 2: Filter Short Words
words = ["cat", "elephant", "dog", "hippopotamus", "ant", "giraffe"]
long_words = [w for w in words if len(w) > 3]
print(long_words)

# Exercise 3: Pass or Fail
scores = [85, 42, 73, 91, 38, 67, 55]
results = ["pass" if s >= 60 else "fail" for s in scores]
print(results)

# Exercise 4: Word Lengths Dict
fruits = ["apple", "banana", "cherry", "kiwi"]
fruit_lengths = {f: len(f) for f in fruits}
print(fruit_lengths)

# Exercise 5: Unique First Letters
cities = ["Tokyo", "Toronto", "London", "Lima", "Paris", "Prague"]
first_letters = {c[0] for c in cities}
print(first_letters)

# Exercise 6: Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)

# Exercise 7: Filter a Dict
inventory = {"apples": 5, "bananas": 0, "cherries": 12, "dates": 0, "eggs": 3}
in_stock = {item: qty for item, qty in inventory.items() if qty > 0}
print(in_stock)
