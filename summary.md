# Python Learning Summary

A quick reference of everything we've covered. Come back here whenever you need a refresher.

---

## Data Types

**Strings** — text in quotes
```python
name = "Alice"
name[0]          # "A"
len(name)        # 5
name.upper()     # "ALICE"
```

**Lists** — ordered, changeable `[]`
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.remove("banana")
fruits[0]        # "apple"
```

**Tuples** — ordered, unchangeable `()`
```python
colors = ("red", "green", "blue")
colors[1]        # "green"
```

**Dicts** — key-value pairs `{k: v}`
```python
person = {"name": "Alice", "age": 25}
person["name"]           # "Alice"
person["email"] = "a@b.com"  # add new key
```

**Sets** — unordered, no duplicates `{}`
```python
nums = {1, 2, 3, 3}     # becomes {1, 2, 3}
nums.add(4)
```

| Type  | Syntax | Ordered? | Changeable? | Duplicates? |
|-------|--------|----------|-------------|-------------|
| List  | `[]`   | Yes      | Yes         | Yes         |
| Tuple | `()`   | Yes      | No          | Yes         |
| Dict  | `{k:v}`| Yes      | Yes         | Keys: No    |
| Set   | `{}`   | No       | Yes         | No          |

---

## Control Flow

**if / elif / else**
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
```
- Check the most specific condition first
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combine with: `and`, `or`, `not`

**for loop**
```python
for fruit in ["apple", "banana"]:
    print(fruit)
```

**range()**
```python
range(5)           # 0, 1, 2, 3, 4
range(1, 6)        # 1, 2, 3, 4, 5
range(0, 10, 2)    # 0, 2, 4, 6, 8 (step by 2)
range(5, 0, -1)    # 5, 4, 3, 2, 1 (countdown)
```

**while loop**
```python
count = 0
while count < 5:
    print(count)
    count += 1      # don't forget this!
```

**while True + break**
```python
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break       # exits the loop
```

**continue** — skip to next iteration
```python
for i in range(10):
    if i % 3 == 0:
        continue    # skip multiples of 3
    print(i)
```

**for/else** — else runs only if no break happened
```python
for i in range(3):
    pw = input("Password: ")
    if pw == "secret":
        print("Access granted!")
        break
else:
    print("Account locked.")
```

**Nested loops**
```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

## Useful Bits

**input()** — get user input (always returns a string)
```python
name = input("Your name: ")
age = int(input("Your age: "))    # convert to number
```

**f-strings** — put variables inside strings
```python
print(f"{name} is {age} years old")
print(f"{2 * 3}")    # can do math inside {}
```

**print(end="")** — stay on same line
```python
print("*", end="")   # no newline
print()               # just a newline
```

**Colons** — needed before indented blocks (`if`, `for`, `while`, `def`, `class`)

**Operators:**
```python
# Arithmetic
5 + 3      # 8   — addition
5 - 3      # 2   — subtraction
5 * 3      # 15  — multiplication
5 / 3      # 1.666 — division (always float)
5 // 3     # 1   — floor division (rounds down, int)
5 % 3      # 2   — remainder/modulo
5 ** 3     # 125 — power (5 to the power of 3)

# Comparison (returns True/False)
==    # equal to
!=    # not equal to
<     # less than
>     # greater than
<=    # less than or equal
>=    # greater than or equal

# Logical
and   # both must be True
or    # at least one True
not   # flips True/False

# Assignment shortcuts
x += 1    # x = x + 1
x -= 1    # x = x - 1
x *= 2    # x = x * 2
x /= 2    # x = x / 2
```

Common uses:
```python
x % 2 == 0    # check if even
x % 2 != 0    # check if odd
x ** 2        # square a number
x ** 0.5      # square root
```

---

## Functions

**Defining and calling**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
```

**Return values** — sends a value back (different from print!)
```python
def add(a, b):
    return a + b

result = add(3, 5)    # result is 8
```
- `print()` → shows on screen, returns None
- `return` → sends value back to the caller

**Default parameters**
```python
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()          # Welcome, Guest!
welcome("Dan")     # Welcome, Dan!
```

**Multiple return values** — assigned by position, not name
```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([3, 1, 7, 2, 9])
# lowest = 1 (first), highest = 9 (second)
```

**Scope** — variables inside a function don't exist outside
```python
def my_func():
    x = 10       # only exists inside
    return x

result = my_func()   # 10 — got the value
print(x)             # ERROR — x doesn't exist here
```

**Built-in functions** you've used so far:
`print()`, `input()`, `int()`, `float()`, `len()`, `range()`, `min()`, `max()`, `enumerate()`

---

## String Formatting

**f-strings** — put variables and expressions inside `{}`
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")
print(f"In 10 years: {age + 10}")    # math inside {}
```

**Decimal places** — `:.Nf` (N = number of decimals)
```python
pi = 3.14159
print(f"{pi:.2f}")     # 3.14
print(f"{pi:.1f}")     # 3.1
```

**Commas** — `:,` for thousands separator
```python
big = 1234567890
print(f"{big:,}")       # 1,234,567,890
print(f"{big:,.2f}")    # 1,234,567,890.00
```

**Percentage** — `:.0%` (multiplies by 100 and adds %)
```python
score = 0.95
print(f"{score:.0%}")   # 95%
```

**Alignment** — `<` left, `>` right, `^` center (with width)
```python
print(f"{'Alice':<10}")   # Alice     (left, 10 wide)
print(f"{30:>5}")         #    30     (right, 5 wide)
print(f"{30:^5}")         #  30      (center, 5 wide)
```

**Multiline strings** — triple quotes `"""`
```python
bio = f"""
Name: {name}
Age: {age}
"""
```

**enumerate()** — get index + value in a loop
```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, 1):   # 1 = start index
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

---

## Basic I/O (File Reading/Writing)

**Writing a file** — `"w"` mode (creates or overwrites)
```python
with open("hello.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Line 2\n")
```

**Reading a file** — `"r"` mode
```python
# Read everything at once
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

# Read into a list
with open("hello.txt", "r") as file:
    lines = file.readlines()    # ['Hello, World!\n', 'Line 2\n']
    print(len(lines))           # count lines
```

**Appending** — `"a"` mode (adds to end, doesn't erase)
```python
with open("hello.txt", "a") as file:
    file.write("New line added\n")
```

**File modes:**
| Mode  | Meaning | Creates? | Erases? |
|-------|---------|----------|---------|
| `"r"` | Read    | No       | No      |
| `"w"` | Write   | Yes      | Yes     |
| `"a"` | Append  | Yes      | No      |

**Always use `with`** — auto-closes the file when done

**`.strip()`** — removes `\n` and extra spaces from a string
```python
line = "hello\n"
clean = line.strip()    # "hello"
```

**Don't reuse variable names** for different file handles:
```python
# Bad:
with open("a.txt", "r") as file:
    with open("b.txt", "w") as file:  # overwrites the first "file"

# Good:
with open("a.txt", "r") as source:
    with open("b.txt", "w") as dest:
```

**Dates**
```python
from datetime import date, timedelta

today = str(date.today())              # "2026-04-12"
yesterday = date.today() - timedelta(days=1)
next_week = date.today() + timedelta(days=7)
```
- `date.today()` — gets today's date
- `timedelta(days=N)` — a duration of time, used for date math

---

## Comprehensions

Shorter way to create lists, dicts, and sets from loops.

**List comprehension**
```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]    # [2, 4, 6, 8, 10]
```

**Filtering** — `if` after `for` (skips items)
```python
evens = [n for n in numbers if n % 2 == 0]    # [2, 4]
```

**Transforming** — `if/else` before `for` (changes items, keeps all)
```python
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
```

**Dict comprehension** — uses `{key: value}`
```python
squares = {n: n ** 2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**Set comprehension** — uses `{}`, no duplicates
```python
first_letters = {word[0] for word in ["Tokyo", "Toronto", "London"]}
# {'T', 'L'}
```

**Dict methods:**
```python
d = {"a": 1, "b": 2}
d.items()     # [("a", 1), ("b", 2)] — key-value pairs
d.keys()      # ["a", "b"]
d.values()    # [1, 2]
```

**Filtering a dict:**
```python
{k: v for k, v in d.items() if v > 0}
```

**Sets vs Lists:**
- Sets: unordered, no duplicates `{1, 2, 3}`
- Lists: ordered, allows duplicates `[1, 2, 2, 3]`

---

## Error Handling

**try / except** — catch errors so your program doesn't crash
```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number!")
```

**Multiple except blocks:**
```python
try:
    result = num1 / num2
except ValueError:
    print("Bad number")
except ZeroDivisionError:
    print("Can't divide by zero")
```

**Common error types:**
| Error | When it happens |
|---|---|
| `ValueError` | Wrong value (`int("hello")`) |
| `ZeroDivisionError` | Dividing by zero |
| `TypeError` | Wrong type (`"hello" + 5`) |
| `FileNotFoundError` | File doesn't exist |
| `IndexError` | List index out of range |
| `KeyError` | Dict key doesn't exist |
| `NameError` | Variable doesn't exist |

**else** — runs only if no error happened
```python
try:
    num = int(input("Number: "))
except ValueError:
    print("Invalid!")
else:
    print(f"You entered {num}")
```

**finally** — always runs no matter what
```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("Not found")
finally:
    print("This always runs")
```

**Getting error message** with `as e`:
```python
except ValueError as e:
    print(f"Error: {e}")
```

**Exception** — catches all errors (use when unsure):
```python
except Exception as e:
    print(f"Something went wrong: {e}")
```
- Better than bare `except:` which hides the error
- Specific errors are still preferred

**Raising errors** — throw your own errors with `raise`:
```python
def get_age(age):
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
    return age
```
- `raise` throws the error OUT to whoever called the function
- The calling code catches it with `try/except`

---

## Modules and Packages

**Three ways to import:**
```python
import math                  # whole module — use math.sqrt()
from math import sqrt, pi   # specific things — use sqrt() directly
import math as m             # alias — use m.sqrt()
```

**Common built-in modules:**
```python
import math
math.sqrt(25)          # 5.0
math.floor(3.7)        # 3
math.ceil(3.2)         # 4
math.pi                # 3.14159...
math.pow(2, 10)        # 1024.0

import random
random.randint(1, 10)         # random int between 1-10
random.choice(["a", "b"])     # pick random item
random.shuffle(my_list)       # shuffle in place (returns None!)

import os
os.getcwd()                   # current directory
os.listdir()                  # list files
os.path.exists("file.txt")   # check if file exists

import string
string.ascii_letters          # a-z + A-Z
string.digits                 # 0-9
```

**Creating your own module** — any .py file is a module:
```python
# my_tools.py
def square(n):
    return n * n
APP_NAME = "My App"

# main.py
import my_tools
my_tools.square(5)       # 25
my_tools.APP_NAME        # "My App"
```

**`if __name__ == "__main__":`** — code inside only runs when file is run directly, not when imported

**Packages** — folders with `__init__.py`:
```python
from my_package.math_tools import double
```

**Exploring modules:**
```python
dir(random)           # list everything in a module
help(random.choice)   # details about a function
```

**`_` as throwaway variable** — when you don't need the loop counter:
```python
for _ in range(5):
    print("hello")
```

---

## Working with Files — CSV and JSON

**CSV** — comma separated values, like a spreadsheet

Reading CSV:
```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)       # reads rows as dicts
    for row in reader:
        print(row["name"], row["age"])  # access by column name
```

- `csv.reader(file)` — rows as lists, access by index `row[0]`
- `csv.DictReader(file)` — rows as dicts, access by name `row["name"]`
- `next(reader)` — skip a row (e.g., header)
- `list(reader)` — convert to list (lets you loop multiple times)

Writing CSV:
```python
with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
```

- Always use `newline=""` when writing CSV
- `writeheader()` writes the column names
- `writerow()` writes one row

**JSON** — nested data (dicts and lists)

Reading JSON:
```python
import json

with open("data.json", "r") as file:
    data = json.load(file)        # file → dict
    print(data["name"])
```

Writing JSON:
```python
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)   # dict → file
```

- `indent=4` makes it readable
- No `newline=""` needed for JSON

String versions (no file):
```python
json.dumps(data)          # dict → string
json.loads(json_string)   # string → dict
```

**CSV vs JSON:**
| | CSV | JSON |
|---|---|---|
| Best for | Tables | Nested data |
| Read | `csv.DictReader()` | `json.load()` |
| Write | `csv.DictWriter()` | `json.dump()` |

**Accessing nested JSON:**
```python
data = {"students": [{"name": "Alice"}, {"name": "Bob"}]}
data["students"]        # the list
data["students"][0]     # first student
data["students"][0]["name"]   # "Alice"
```

---

## Object-Oriented Programming (OOP)

**Class** = blueprint. **Object** = thing created from the blueprint.

```python
class Dog:
    def __init__(self, n, a):      # runs when object is created
        self.dog_name = n          # attribute (saved permanently)
        self.dog_age = a           # attribute

    def bark(self):                # method
        print(f"{self.dog_name} says Woof!")

dog1 = Dog("Buddy", 3)            # creates object
dog1.bark()                        # calls method
```

**Parameters vs Attributes:**
- Parameter (`n`) — temporary, brings value in, disappears after `__init__`
- Attribute (`self.dog_name`) — permanent, saved on the object
- `self.dog_name = n` copies the parameter value to the attribute

**Where parameters go:**
- `Dog("Buddy", 3)` → parameters go in `__init__`
- `dog.fetch("ball")` → parameters go in that method
- Method parameters don't need to be in `__init__`

**self** = placeholder for whatever object calls the method:
```python
dog1.bark()    # self = dog1
dog2.bark()    # self = dog2
```

**Inheritance** — child gets everything from parent:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("generic sound")

class Dog(Animal):              # inherits from Animal
    def speak(self):            # overrides parent's speak
        print(f"{self.name} says Woof!")
```

**super()** — call parent's `__init__` when child has extra attributes:
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # parent saves name
        self.breed = breed          # child saves breed
```
- No extra attributes in child → no `__init__` needed, parent's is inherited
- Extra attributes in child → need `__init__` + `super()`

**Polymorphism** — same method name, different behavior:
```python
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    animal.speak()    # each does its own version
```

**Composition** — one object contains other objects (NOT inheritance):
```python
class Classroom:
    def __init__(self):
        self.students = []          # contains Student objects
    def add_student(self, student):
        self.students.append(student)

room = Classroom()
room.add_student(s1)    # s1 is a Student object inside Classroom
```

**Encapsulation** — `_` prefix means "private, use methods instead":
```python
self._balance = 0           # convention: don't access directly
account.get_balance()       # use methods instead
```

**`__str__`** — controls what `print(object)` shows:
```python
def __str__(self):
    return f"{self.name}, age {self.age}"    # use return, not print
```

**Common dunder methods:**
| Method | Triggered by |
|---|---|
| `__init__` | `Dog("Buddy", 3)` |
| `__str__` | `print(dog1)` |
| `__len__` | `len(obj)` |
| `__eq__` | `obj1 == obj2` |

**Abstraction** — force children to implement methods:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):        # children MUST implement this
        pass

    def describe(self):    # regular method — children inherit this
        print(f"Area: {self.area()}")
```
- `ABC` — makes class abstract
- `@abstractmethod` — marks method as required
- Can't create object from abstract class directly
- Children that forget a method → ERROR

**Four pillars of OOP:**
1. Encapsulation — hide data, use methods
2. Inheritance — child gets from parent
3. Polymorphism — same method, different behavior
4. Abstraction — force required methods

---

## Iterators and Generators

**iter() and next()** — how loops work behind the scenes:
```python
numbers = [1, 2, 3]
it = iter(numbers)
print(next(it))    # 1
print(next(it))    # 2
print(next(it))    # 3
print(next(it))    # StopIteration error
```

**Custom iterator class** — needs `__iter__` and `__next__`:
```python
class MyRange:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self              # "I am the iterator"

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # stop the loop
        value = self.current
        self.current += self.step
        return value
```

**Generator function** — simpler way using `yield`:
```python
def count_up(start, end):
    current = start
    while current <= end:
        yield current        # pause, give value
        current += 1         # resume here next time
```
- `yield` = pause and deliver value, come back later
- `return` = stop forever
- Any function with `yield` is a generator

**Generator expression** — one-liner, like list comprehension with `()`:
```python
# List comprehension — all in memory
[x ** 2 for x in range(10)]

# Generator expression — one at a time
(x ** 2 for x in range(10))

# Use with sum(), etc:
print(sum(x ** 2 for x in numbers if x % 2 != 0))
```

**When to use:**
- Small data → regular list
- Large data, one-time loop → generator

---

## String Indexing

Access individual characters by position (starts at 0):
```python
word = "hello"
word[0]    # "h"
word[1]    # "e"
word[4]    # "o"
```

---

## Methods vs Functions

**Functions** — standalone:
```python
print("hello")
len("hello")
```

**Methods** — attached to a value with a dot:
```python
"hello".upper()          # "HELLO"
"hello".isdigit()        # False
"5".isdigit()            # True
"hello".startswith("he") # True
```

Methods are built into Python — every string/list/etc. comes with them.

---

## String Concatenation with +=

```python
result = ""
result += "h"    # "h"
result += "i"    # "hi"
# same as: result = result + "i"
```

---

## Reserved Keywords

These names are taken by Python — can't use them as variable names:
`pass`, `if`, `else`, `for`, `while`, `return`, `def`, `class`, `True`, `False`, `None`, `break`, `continue`, `import`
