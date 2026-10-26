# List, Dict, and Set Comprehensions

Comprehensions are a shorter way to create lists, dicts, and sets.
Instead of writing a loop over multiple lines, you do it in one line.

---

## 1. List Comprehension

### The long way (what you already know):

```python
numbers = [1, 2, 3, 4, 5]
doubled = []
for n in numbers:
    doubled.append(n * 2)
print(doubled)    # [2, 4, 6, 8, 10]
```

### The comprehension way (same result, one line):

```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)    # [2, 4, 6, 8, 10]
```

The pattern is:
```
[expression for item in iterable]
```

- `expression` — what to do with each item (e.g., `n * 2`)
- `item` — the variable for each element (e.g., `n`)
- `iterable` — what you're looping through (e.g., `numbers`)

### More examples:

```python
# Squares
squares = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# Uppercase words
words = ["hello", "world"]
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']

# Lengths of words
names = ["Alice", "Bob", "Charlie"]
lengths = [len(name) for name in names]
# [5, 3, 7]
```

---

## 2. List Comprehension with Condition (Filtering)

You can add `if` to filter items:

```
[expression for item in iterable if condition]
```

### The long way:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)    # [2, 4, 6, 8, 10]
```

### The comprehension way:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)    # [2, 4, 6, 8, 10]
```

### More examples:

```python
# Words longer than 3 characters
words = ["hi", "hello", "hey", "world"]
long_words = [w for w in words if len(w) > 3]
# ['hello', 'world']

# Positive numbers only
nums = [-3, -1, 0, 2, 5, -4, 8]
positive = [n for n in nums if n > 0]
# [2, 5, 8]
```

---

## 3. List Comprehension with if/else

When you want to transform items differently based on a condition,
the `if/else` goes **before** the `for`:

```
[expression_if_true if condition else expression_if_false for item in iterable]
```

```python
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
# ['odd', 'even', 'odd', 'even', 'odd']
```

Note the difference:
- **Filtering** (if after for): `[n for n in nums if n > 0]` — skips items
- **Transforming** (if before for): `["yes" if n > 0 else "no" for n in nums]` — changes items

---

## 4. Dict Comprehension

Same idea but creates a dictionary. Uses `{}` and `key: value`:

```
{key: value for item in iterable}
```

But first, you need to know how to loop through a dictionary.
Every dict has these built-in methods:

```python
scores = {"Alice": 85, "Bob": 42, "Charlie": 91}

scores.keys()     # ["Alice", "Bob", "Charlie"] — just the keys
scores.values()   # [85, 42, 91] — just the values
scores.items()    # [("Alice", 85), ("Bob", 42), ("Charlie", 91)] — both
```

- `scores` is YOUR variable name — whatever you named your dict
- `.items()` is a method that ALL dicts have — it gives you key-value pairs

You can loop through `.items()` like this:

```python
for name, score in scores.items():
    print(name, score)
# Alice 85
# Bob 42
# Charlie 91
```

Now, dict comprehensions:

```python
# Create a dict of number: square
squares = {n: n ** 2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Name: length of name
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# With filtering — using .items() to get key and value
scores = {"Alice": 85, "Bob": 42, "Charlie": 91}
passed = {name: score for name, score in scores.items() if score >= 50}
# {'Alice': 85, 'Charlie': 91}
```

---

## 5. Set Comprehension

Same as list comprehension but uses `{}` and produces a set (no duplicates):

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_doubled = {n * 2 for n in numbers}
# {2, 4, 6, 8} — no duplicates!

# First letters (unique)
names = ["Alice", "Anna", "Bob", "Charlie", "Carl"]
first_letters = {name[0] for name in names}
# {'A', 'B', 'C'}
```

---

## 6. When to Use Comprehensions

Use them when:
- You're creating a new list/dict/set from an existing one
- The logic is simple (one expression, maybe one condition)

Don't use them when:
- The logic is complex (multiple conditions, nested loops)
- It makes the code hard to read

```python
# Good — simple and readable
evens = [n for n in range(20) if n % 2 == 0]

# Bad — too complex, use a regular loop instead
result = [x * y for x in range(10) for y in range(10) if x != y and x + y > 5]
```

If a comprehension is hard to read, a regular loop is better.
