# Working with Files — CSV, JSON, and Text

You already know how to read/write text files. Now we'll work with
structured data formats: CSV and JSON. These are used everywhere.

---

## 1. CSV Files

CSV = Comma Separated Values. It's like a spreadsheet in text form.

A CSV file looks like this:
```
name,age,city
Alice,30,New York
Bob,25,London
Charlie,35,Tokyo
```

### Reading a CSV file:

```python
import csv

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# ['name', 'age', 'city']
# ['Alice', '30', 'New York']
# ['Bob', '25', 'London']
# ['Charlie', '35', 'Tokyo']
```

- `csv.reader(file)` reads the file and splits each line by commas
- Each `row` is a list of strings
- Note: numbers come as strings — use `int()` or `float()` to convert

### Accessing specific columns:

```python
import csv

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)    # skip the header row
    for row in reader:
        name = row[0]
        age = int(row[1])
        city = row[2]
        print(f"{name} is {age} years old from {city}")
```

- `next(reader)` skips one row (the header)
- `row[0]`, `row[1]`, `row[2]` access columns by index

### Reading CSV as dictionaries:

```python
import csv

with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])
# Alice 30
# Bob 25
# Charlie 35
```

- `DictReader` uses the header row as keys
- Access columns by name instead of index — much clearer

### Writing a CSV file:

```python
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
```

- `csv.writer(file)` creates a writer
- `writer.writerow(row)` writes one row
- `newline=""` prevents extra blank lines on some systems

### Writing CSV from dictionaries:

```python
import csv

people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "London"},
]

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
    writer.writeheader()    # writes the header row
    for person in people:
        writer.writerow(person)
```

---

## 2. JSON Files

JSON = JavaScript Object Notation. It looks very similar to Python dicts and lists.

A JSON file looks like this:
```json
{
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}
```

### Reading a JSON file:

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])       # Alice
print(data["hobbies"])    # ['reading', 'coding']
```

- `json.load(file)` reads the file and converts it to a Python dict/list
- Then you use it like a normal dict

### Writing a JSON file:

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

- `json.dump(data, file)` writes the dict to a file
- `indent=4` makes it pretty-printed (readable), without it everything is on one line

### Converting between JSON strings and Python:

```python
import json

# Python dict → JSON string
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)    # '{"name": "Alice", "age": 30}'

# JSON string → Python dict
json_string = '{"name": "Bob", "age": 25}'
data = json.loads(json_string)
print(data["name"])   # Bob
```

- `json.dumps()` — dict to string (the "s" = string)
- `json.loads()` — string to dict (the "s" = string)
- `json.dump()` — dict to file
- `json.load()` — file to dict

---

## 3. Quick Comparison

| Feature | CSV | JSON |
|---------|-----|------|
| Looks like | Spreadsheet | Python dict/list |
| Best for | Tables (rows and columns) | Nested/complex data |
| Module | `import csv` | `import json` |
| Read | `csv.reader()` / `csv.DictReader()` | `json.load()` |
| Write | `csv.writer()` / `csv.DictWriter()` | `json.dump()` |

Use CSV when your data is flat (like a table).
Use JSON when your data is nested (like dicts inside dicts).
