# Decorators

You already saw `@abstractmethod` — that's a decorator. Now let's learn what decorators actually are and how to make your own.

---

## 1. Functions are Objects

In Python, functions are just like any other value — you can store them in variables, pass them around, and even put them inside other functions.

```python
def greet():
    print("Hello!")

# Store function in a variable (no parentheses = don't call it)
say_hi = greet
say_hi()    # Hello!

# Pass function to another function
def run_twice(func):
    func()
    func()

run_twice(greet)
# Hello!
# Hello!
```

- `greet` without `()` = the function itself (an object)
- `greet()` with `()` = calling/running the function

---

## 2. What is a Decorator?

A decorator is a function that takes another function, adds something to it, and returns a new version.

```python
def make_loud(func):
    def wrapper():
        print("!!!")
        func()
        print("!!!")
    return wrapper

@make_loud
def greet():
    print("Hello")

greet()
# !!!
# Hello
# !!!
```

What happened:
1. `@make_loud` takes `greet` and passes it to `make_loud()`
2. `make_loud` creates a new function `wrapper` that adds `!!!` before and after
3. `greet` is now replaced with `wrapper`

Without the `@` syntax, it's the same as:

```python
def greet():
    print("Hello")

greet = make_loud(greet)    # same as @make_loud
```

---

## 3. Decorators with Arguments

If the original function takes arguments, the wrapper needs `*args, **kwargs` to pass them through:

```python
def make_loud(func):
    def wrapper(*args, **kwargs):
        print("!!!")
        result = func(*args, **kwargs)
        print("!!!")
        return result
    return wrapper

@make_loud
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# !!!
# Hello, Alice
# !!!
```

- `*args` — catches any number of positional arguments
- `**kwargs` — catches any number of keyword arguments
- This makes the decorator work with ANY function, no matter what arguments it takes

---

## 4. Practical Example: Timer Decorator

A decorator that measures how long a function takes:

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)    # wait 1 second

slow_function()
# slow_function took 1.0012 seconds
```

- `func.__name__` gives the function's name as a string
- `time.time()` gives the current time in seconds
- This is useful for finding slow parts of your code

---

## 5. Practical Example: Logger Decorator

A decorator that logs every time a function is called:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# Calling add with args=(3, 5)
# add returned 8
```

---

## 6. Stacking Decorators

You can use multiple decorators on one function:

```python
def decorator_A(func):
    def wrapper_A(*args, **kwargs):
        print("A - before")
        result = func(*args, **kwargs)
        print("A - after")
        return result
    return wrapper_A

def decorator_B(func):
    def wrapper_B(*args, **kwargs):
        print("B - before")
        result = func(*args, **kwargs)
        print("B - after")
        return result
    return wrapper_B

@decorator_A
@decorator_B
def say_hello():
    print("Hello!")

say_hello()
```

### What Python does with the `@` decorators:

```python
# Step 1: decorator_B receives say_hello
decorator_B(say_hello)
# func inside decorator_B = say_hello
# returns wrapper_B
# say_hello is now wrapper_B

# Step 2: decorator_A receives wrapper_B
decorator_A(wrapper_B)
# func inside decorator_A = wrapper_B
# returns wrapper_A
# say_hello is now wrapper_A
```

The key: each decorator's `func` is set when the `@` is applied.
- decorator_A's `func` = wrapper_B
- decorator_B's `func` = real say_hello

### What happens when you call `say_hello()`:

You're calling wrapper_A:

```python
# wrapper_A runs:
print("A - before")                  # 1. prints: A - before
result = func(*args, **kwargs)       # 2. func = wrapper_B, so calls wrapper_B:

    # wrapper_B runs:
    print("B - before")              # 3. prints: B - before
    result = func(*args, **kwargs)   # 4. func = real say_hello, so calls it:

        # real say_hello runs:
        print("Hello!")              # 5. prints: Hello!

    print("B - after")              # 6. prints: B - after
    # wrapper_B is done, goes back to wrapper_A

print("A - after")                  # 7. prints: A - after
```

### Why does it "go back" to A after B finishes?

Because wrapper_B was called from wrapper_A's `func()` line. When a function call finishes, the code continues to the next line — just like any function:

```python
def outer():
    print("outer - before")
    inner()                      # calls inner, WAITS for it to finish
    print("outer - after")       # runs after inner is done

def inner():
    print("inside inner")

outer()
# outer - before
# inside inner
# outer - after    ← continues where it left off
```

### Output:

```
A - before
B - before
Hello!
B - after
A - after
```

Top decorator (A) starts first and finishes last. Bottom decorator (B) starts second and finishes second. The real function runs in the middle.

---

## 7. When to Use Decorators

Common uses:
- Timing functions (how long they take)
- Logging (recording what functions are called)
- Authentication (checking if user is logged in)
- Caching (remembering results to avoid recalculating)
- Validation (checking inputs before running)

The key idea: decorators let you add behavior to functions without changing the function itself.
