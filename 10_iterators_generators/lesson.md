# Iterators and Generators

## 1. What is an Iterator?

You've been using iterators without knowing it. Every time you use a `for` loop, you're using an iterator.

```python
for item in [1, 2, 3]:
    print(item)
```

An iterator is any object that you can loop through one item at a time. Lists, strings, dicts, files — they're all iterable.

### How it works behind the scenes:

```python
numbers = [1, 2, 3]
it = iter(numbers)     # create an iterator from the list

print(next(it))        # 1 — get next item
print(next(it))        # 2
print(next(it))        # 3
print(next(it))        # ERROR — StopIteration (no more items)
```

- `iter()` — creates an iterator from an iterable
- `next()` — gets the next item
- When there are no more items, it raises `StopIteration`

That's exactly what a `for` loop does automatically — it calls `iter()`, then keeps calling `next()` until `StopIteration`.

---

## 2. Creating Your Own Iterator

You can make any class iterable by adding `__iter__` and `__next__` methods:

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self        # the object itself is the iterator

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in CountUp(1, 5):
    print(num)
# 1, 2, 3, 4, 5
```

- `__iter__` — returns the iterator object (usually `self`)
- `__next__` — returns the next value, raises `StopIteration` when done

This is useful but writing a whole class just to iterate is a lot of code. That's where generators come in.

---

## 3. What is a Generator?

A generator is a simpler way to create an iterator. Instead of a class with `__iter__` and `__next__`, you write a function with `yield`.

```python
def count_up(start, end):
    current = start
    while current <= end:
        yield current       # pause here, give this value
        current += 1        # resume here next time

for num in count_up(1, 5):
    print(num)
# 1, 2, 3, 4, 5
```

Same result as the class above, but much shorter!

### How `yield` works:

`yield` is like `return`, but instead of ending the function, it **pauses** it:

1. Function runs until it hits `yield` → gives the value
2. Function pauses — remembers where it was
3. Next time you ask for a value → function resumes from where it paused
4. Repeats until the function ends

```python
def simple():
    print("Step 1")
    yield "A"
    print("Step 2")
    yield "B"
    print("Step 3")
    yield "C"

for letter in simple():
    print(letter)

# Step 1
# A
# Step 2
# B
# Step 3
# C
```

Each `yield` pauses the function. The `for` loop resumes it each time.

---

## 4. Generator vs Regular Function

```python
# Regular function — builds entire list in memory
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result                  # returns everything at once

# Generator — produces one item at a time
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2               # gives one item, pauses

# Both work the same in a for loop:
for sq in get_squares_list(5):
    print(sq)

for sq in get_squares_gen(5):
    print(sq)
```

The difference: the list version creates ALL items in memory at once. The generator creates them one at a time — much better for large data.

```python
# This would use tons of memory:
big_list = get_squares_list(10_000_000)    # 10 million items in memory!

# This uses almost no memory:
big_gen = get_squares_gen(10_000_000)      # items created one at a time
```

---

## 5. Generator Expressions

Just like list comprehensions, but with `()` instead of `[]`:

```python
# List comprehension — creates entire list in memory
squares_list = [x ** 2 for x in range(10)]

# Generator expression — creates items one at a time
squares_gen = (x ** 2 for x in range(10))
```

```python
# You can loop through both:
for sq in squares_gen:
    print(sq)

# Or convert generator to list:
squares = list(squares_gen)

# Or use with functions like sum:
total = sum(x ** 2 for x in range(10))    # no extra brackets needed
print(total)    # 285
```

---

## 6. Practical Examples

### Reading a large file line by line:

```python
def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

for line in read_lines("big_file.txt"):
    print(line)
```

### Generating an infinite sequence:

```python
def count_forever(start=0):
    current = start
    while True:          # never ends!
        yield current
        current += 1

# Use with caution — need to break out:
for num in count_forever():
    if num > 10:
        break
    print(num)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

### Filtering data:

```python
def even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in even_numbers(nums):
    print(n)
# 2, 4, 6, 8, 10
```

---

## 7. When to Use What

| Use | When |
|---|---|
| Regular list | Small data, need to access items multiple times |
| Generator function (`yield`) | Large data, complex logic, one-time iteration |
| Generator expression `()` | Simple one-liners, like list comprehension but memory-efficient |

Key rule: if you only need to loop through data once and the data could be large, use a generator.
