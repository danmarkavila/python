# Modules and Packages

A module is just a Python file that contains code you can reuse.
Instead of writing everything in one file, you split it into separate files and import what you need.

---

## 1. Importing a Module

Python comes with many built-in modules. You've already used some:

```python
from datetime import date       # you used this in the diary exercise
import os                       # you used this to check if a file exists
```

### Three ways to import:

```python
# Way 1: import the whole module
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...

# Way 2: import specific things
from math import sqrt, pi
print(sqrt(16))          # 4.0 — no need for math. prefix
print(pi)                # 3.14159...

# Way 3: import with a nickname (alias)
import math as m
print(m.sqrt(16))        # 4.0
```

- Way 1: safe, clear where things come from (`math.sqrt`)
- Way 2: shorter, but less clear where it came from
- Way 3: useful for long module names

---

## 2. Common Built-in Modules

```python
import math
math.sqrt(25)       # 5.0 — square root
math.floor(3.7)     # 3 — round down
math.ceil(3.2)      # 4 — round up
math.pi             # 3.14159...

import random
random.randint(1, 10)      # random number between 1 and 10
random.choice(["a", "b"])  # pick a random item from a list
random.shuffle([1, 2, 3])  # shuffle a list in place

import os
os.path.exists("file.txt")   # check if file exists
os.getcwd()                   # get current working directory
os.listdir(".")               # list files in a directory

from datetime import date, timedelta
date.today()                          # today's date
date.today() + timedelta(days=7)      # 7 days from now

import string
string.ascii_lowercase    # 'abcdefghijklmnopqrstuvwxyz'
string.digits             # '0123456789'
```

---

## 3. Creating Your Own Module

Any Python file is a module. Just create a file and import it.

Create a file called `helpers.py`:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

Now use it in another file in the same folder:

```python
# main.py
import helpers

print(helpers.greet("Alice"))    # Hello, Alice!
print(helpers.add(3, 5))        # 8
print(helpers.PI)                # 3.14159
```

Or import specific things:

```python
from helpers import greet, PI

print(greet("Bob"))    # Hello, Bob!
print(PI)              # 3.14159
```

---

## 4. The `if __name__ == "__main__"` Pattern

When you import a module, Python runs ALL the code in that file. This can be a problem:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

# This runs when you import helpers!
print(greet("Test"))
```

To prevent code from running on import, use this pattern:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This only runs when you run helpers.py directly
    # NOT when you import it
    print(greet("Test"))
```

- `__name__` is a special variable Python sets automatically
- When you run a file directly: `__name__` = `"__main__"`
- When you import a file: `__name__` = the module name (e.g., `"helpers"`)

---

## 5. Packages (Folders of Modules)

A package is a folder that contains multiple modules.

```
my_package/
    __init__.py      ← makes the folder a package (can be empty)
    math_tools.py
    string_tools.py
```

```python
# __init__.py can be empty, or import things for convenience

# math_tools.py
def double(n):
    return n * 2

# string_tools.py
def shout(text):
    return text.upper() + "!"
```

Using the package:

```python
from my_package.math_tools import double
from my_package.string_tools import shout

print(double(5))        # 10
print(shout("hello"))   # HELLO!
```

- The `__init__.py` file tells Python "this folder is a package"
- You use dot notation to access modules inside: `my_package.math_tools`

---

## 6. Installing External Packages

Python has thousands of packages made by other people. Install them with `pip`:

```bash
pip install requests        # for making web requests
pip install pandas          # for data analysis
pip install flask           # for web apps
```

Then import and use them:

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)
```

To see what's installed:

```bash
pip list
```

We'll use external packages more later. For now, focus on built-in modules and creating your own.
