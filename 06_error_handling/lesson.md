# Error Handling in Python

When something goes wrong in your code, Python raises an **error** (also called an **exception**).
Instead of letting your program crash, you can **catch** the error and handle it.

---

## 1. Common Errors

```python
# TypeError — wrong type
"hello" + 5                    # can't add string and int

# ValueError — right type, wrong value
int("hello")                   # can't convert "hello" to a number

# ZeroDivisionError — dividing by zero
10 / 0

# FileNotFoundError — file doesn't exist
open("nonexistent.txt", "r")

# IndexError — list index out of range
my_list = [1, 2, 3]
my_list[10]

# KeyError — dict key doesn't exist
my_dict = {"name": "Alice"}
my_dict["age"]

# NameError — variable doesn't exist
print(undefined_variable)
```

---

## 2. try / except

Catches an error so your program doesn't crash.

```python
try:
    num = int(input("Enter a number: "))
    print(f"You entered {num}")
except:
    print("That's not a valid number!")
```

- `try:` — "try running this code"
- `except:` — "if an error happens, run this instead"

Without try/except, typing "hello" would crash the program.
With it, the user sees a friendly message instead.

---

## 3. Catching Specific Errors

It's better to catch **specific** errors so you know what went wrong:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

- If user types "hello" → `ValueError` is caught
- If user types "0" → `ZeroDivisionError` is caught
- Each error gets its own message

---

## 4. The `else` Block

Runs only if **no error** happened:

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Not a valid number!")
else:
    print(f"Success! You entered {num}")
```

- Error happens → `except` runs, `else` is skipped
- No error → `except` is skipped, `else` runs

---

## 5. The `finally` Block

Runs **no matter what** — error or not:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs.")
```

- `finally` is useful for cleanup (closing files, connections, etc.)
- It runs whether the try succeeded or failed

---

## 6. Full Structure

```python
try:
    # code that might cause an error
except SomeError:
    # handle the error
else:
    # runs if NO error happened
finally:
    # ALWAYS runs
```

You don't need all four — `try/except` is the most common combo.

---

## 7. Getting the Error Message

You can capture the error message using `as`:

```python
try:
    num = int("hello")
except ValueError as e:
    print(f"Error: {e}")
# Error: invalid literal for int() with base 10: 'hello'
```

- `as e` stores the error in a variable called `e`
- Useful for debugging or showing the user what went wrong

### Catching any error with Exception

If you're unsure which specific error to catch, use `Exception`:

```python
try:
    # some code you're not sure about
    result = int(input("Enter a number: "))
except Exception as e:
    print(f"Something went wrong: {e}")
```

- `Exception` is the parent of all errors — catches everything
- `as e` still shows you what went wrong
- Better than bare `except:` which hides the error message

Best practice:
- Use **specific errors** when you know what could go wrong (recommended)
- Use **`Exception as e`** when you're unsure (okay, at least you see the message)
- Avoid **bare `except:`** — it hides problems and makes debugging hard

---

## 8. Raising Your Own Errors

You can create your own errors with `raise`:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)    # Age cannot be negative!
```

- `raise` says "something is wrong, stop here"
- Useful inside functions to reject bad input

---

## 9. Practical Example: Safe Input

A function that keeps asking until the user enters a valid number:

```python
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

age = get_number("Enter your age: ")
print(f"Your age is {age}")
```

This is much better than letting the program crash when the user types something wrong.
