# Decorator Answers — try solving them yourself first!

import time

# Exercise 1: Shout Decorator
def shout(func):
    def wrapper():
        print(">>>")
        func()
        print("<<<")
    return wrapper

@shout
def hello():
    print("Hello, World!")

hello()


# Exercise 2: Repeat Decorator
def repeat(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return wrapper

@repeat
def say_hi():
    print("Hi!")

say_hi()


# Exercise 3: Timer Decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def big_loop():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

big_loop()


# Exercise 4: Logger with Arguments
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name):
    return f"Hello, {name}!"

add(3, 5)
greet("Alice")


# Exercise 5: Access Control
logged_in = False

def require_login(func):
    def wrapper(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied! Please log in.")
    return wrapper

@require_login
def view_profile():
    print("Welcome to your profile!")

view_profile()          # Access denied!
logged_in = True
view_profile()          # Welcome to your profile!
