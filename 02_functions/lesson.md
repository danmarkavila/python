# Functions in Python

## What is a function?

A function is a reusable block of code that does a specific task.
Instead of writing the same code over and over, you put it in a function and call it whenever you need it.

---

## 1. Defining and Calling a Function

```python
def greet():
    print("Hello!")

greet()    # calling the function → prints "Hello!"
greet()    # can call it as many times as you want
```

- `def` — keyword that means "I'm defining a function"
- `greet` — the name of the function (you choose this)
- `()` — parentheses (for parameters, more on that next)
- `:` — colon, just like if/for/while
- The code inside is indented

---

## 2. Parameters and Arguments

Parameters let you pass data into a function.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice!
greet("Bob")      # Hello, Bob!
```

- `name` is a **parameter** (the variable in the definition)
- `"Alice"` is an **argument** (the value you pass when calling)

### Multiple parameters:

```python
def add(a, b):
    print(a + b)

add(3, 5)    # 8
add(10, 20)  # 30
```

---

## 3. Return Values

Functions can send a result back using `return`.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)    # 8
```

Without `return`, the function returns `None` (nothing).

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")    # prints "Hello, Alice!"
print(result)              # None — because greet doesn't return anything
```

**Key difference:**
- `print()` — shows something on screen
- `return` — sends a value back to whoever called the function

---

## 4. Default Parameters

You can give parameters a default value.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()          # Hello, World!
greet("Alice")   # Hello, Alice!
```

If no argument is passed, it uses the default.

---

## 5. Multiple Return Values

A function can return more than one value.
`min()` and `max()` are built-in Python functions — you don't need to create them.

```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([3, 1, 7, 2, 9])
print(lowest)     # 1
print(highest)    # 9
```

**Important:** the values are assigned by **position**, not by name.

```python
return min(numbers), max(numbers)
#      ^ first        ^ second

lowest, highest = min_max([3, 1, 7, 2, 9])
# ^ first  ^ second
```

- `lowest` gets the first returned value (min)
- `highest` gets the second returned value (max)
- The variable names are your choice — what matters is the order

---

## 6. Scope

Variables created inside a function only exist inside that function.

```python
def my_function():
    x = 10       # x only exists inside this function
    print(x)

my_function()    # 10
print(x)         # ERROR — x doesn't exist out here
```

Variables outside a function can be read inside, but not changed:

```python
name = "Alice"

def greet():
    print(f"Hello, {name}")   # this works — reading is fine

greet()    # Hello, Alice
```
