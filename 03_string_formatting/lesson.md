# String Formatting in Python

You already know f-strings! This lesson covers them in more depth,
plus other ways to format strings.

---

## 1. f-strings (the main one you'll use)

Put `f` before the string, and use `{}` for variables or expressions.

```python
name = "Alice"
age = 25

print(f"My name is {name}")           # My name is Alice
print(f"I am {age} years old")        # I am 25 years old
print(f"Next year I'll be {age + 1}") # Next year I'll be 26
```

### Math inside f-strings:
```python
price = 49.99
tax = 0.1
print(f"Total: {price + (price * tax)}")   # Total: 54.989
```

### Calling functions/methods inside f-strings:
```python
name = "alice"
print(f"Hello, {name.upper()}")    # Hello, ALICE
print(f"Length: {len(name)}")      # Length: 5
```

---

## 2. Formatting Numbers

### Round decimals:
```python
pi = 3.14159
print(f"{pi:.2f}")     # 3.14  (2 decimal places)
print(f"{pi:.4f}")     # 3.1416 (4 decimal places)
```

### Add commas to large numbers:
```python
population = 1000000
print(f"{population:,}")    # 1,000,000
```

### Percentage:
```python
score = 0.85
print(f"{score:.0%}")    # 85%
print(f"{score:.1%}")    # 85.0%
```

### Padding/alignment:
```python
name = "Alice"
print(f"{name:<10}")    # "Alice     " (left align, 10 chars wide)
print(f"{name:>10}")    # "     Alice" (right align)
print(f"{name:^10}")    # "  Alice   " (center)
```

---

## 3. .format() method (older way)

Works like f-strings but uses `.format()` instead:

```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))
# My name is Alice and I am 25 years old

# With numbered positions:
print("{0} is {1}. {0} likes Python.".format(name, age))
# Alice is 25. Alice likes Python.
```

You'll see this in older code. f-strings are preferred for new code.

---

## 4. String Concatenation (the basic way)

Joining strings with `+`:

```python
first = "Hello"
last = "World"
print(first + " " + last)    # Hello World
```

Problem: you can't mix strings and numbers:
```python
age = 25
print("I am " + age)          # ERROR!
print("I am " + str(age))     # I am 25 (convert to string first)
```

This is why f-strings are better — they handle conversion automatically.

---

## 5. Multiline Strings

Use triple quotes for strings that span multiple lines:

```python
message = """Hello,
This is a message
that spans multiple lines."""

print(message)
```

Works with f-strings too:

```python
name = "Alice"
age = 25
bio = f"""
Name: {name}
Age: {age}
Status: Active
"""
print(bio)
```

---

## 6. Escape Characters

Special characters inside strings:

```python
print("Hello\nWorld")     # \n = new line
# Hello
# World

print("Hello\tWorld")     # \t = tab
# Hello   World

print("She said \"hi\"")  # \" = quote inside quotes
# She said "hi"

print("C:\\Users\\name")  # \\ = backslash
# C:\Users\name
```
