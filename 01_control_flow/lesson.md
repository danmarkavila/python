# Control Flow in Python

## 1. if / elif / else

Used to make decisions in your code.

```python
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

Key points:
- Python uses **indentation** (4 spaces) instead of braces `{}`
- `elif` is short for "else if"
- `else` is optional
- You can have as many `elif` blocks as you want

### Comparison operators:
- `==` equal to
- `!=` not equal to
- `<` `>` `<=` `>=` less/greater than
- `in` — check if something is inside a list/string
- `not`, `and`, `or` — combine conditions

```python
name = "Alice"
score = 85

if name == "Alice" and score >= 80:
    print("Alice passed with a good score!")
```

---

## 2. for loops

Used to repeat something for each item in a sequence.

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a range of numbers
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step by 2)
    print(i)
```

---

## 3. while loops

Keeps running as long as a condition is True.

```python
count = 0
while count < 5:
    print(count)
    count += 1    # don't forget this or it loops forever!
```

---

## 4. break and continue

- `break` — exit the loop immediately
- `continue` — skip to the next iteration

```python
# break example: stop when we find "banana"
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        break
    print(fruit)
# Output: apple

# continue example: skip "banana"
for fruit in ["apple", "banana", "cherry"]:
    if fruit == "banana":
        continue
    print(fruit)
# Output: apple, cherry
```

---

## 5. Nested loops

A loop inside a loop.

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```
