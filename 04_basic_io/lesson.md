# Basic I/O — File Reading and Writing

So far, all the data in your programs disappears when the program ends.
Files let you **save data permanently** — so it's still there next time you run your program.

---

## 1. Writing to a File

```python
with open("hello.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
```

Let's break this down piece by piece:

- `open("hello.txt", "w")` — opens a file called "hello.txt"
  - If the file doesn't exist, Python **creates** it
  - If it already exists, Python **erases everything** in it and starts fresh
- `"w"` — this is the **mode**, "w" means write
- `as file` — gives the opened file a nickname so you can use it
  - `file` is just a variable name, you could call it `f` or `my_file`
- `file.write(...)` — writes text into the file
- `\n` — this is the newline character, like pressing Enter
  - Without `\n`, everything would be on one line
- `with` — automatically closes the file when the indented block ends

After running this, a file called "hello.txt" will appear with:
```
Hello, World!
This is line 2.
```

### Writing multiple lines at once:

```python
with open("hello.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")
```

This creates:
```
Line 1
Line 2
Line 3
```

### Common mistake — forgetting \n:

```python
with open("hello.txt", "w") as file:
    file.write("Hello")
    file.write("World")
```

The file will contain: `HelloWorld` (all on one line!)

Add `\n` to get separate lines:
```python
    file.write("Hello\n")
    file.write("World\n")
```

---

## 2. Reading a File

### Read the entire file at once:

```python
with open("hello.txt", "r") as file:
    content = file.read()
    print(content)
```

- `"r"` — read mode (this is the default, so you can also write `open("hello.txt")`)
- `file.read()` — reads EVERYTHING in the file as one big string
- The result is stored in `content`, then printed

### Read line by line (useful for big files):

```python
with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")
```

- This loops through the file one line at a time
- `end=""` is needed because each line already has `\n` at the end
  - Without it, you'd get double spacing (one `\n` from the file + one from `print`)

### Read all lines into a list:

```python
with open("hello.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

Output: `['Hello, World!\n', 'This is line 2.\n']`

- Each line becomes an item in the list
- Notice the `\n` is included in each string
- You can use `len(lines)` to count how many lines

### Removing \n from lines:

```python
with open("hello.txt", "r") as file:
    for line in file:
        clean_line = line.strip()    # removes \n and extra spaces
        print(clean_line)
```

- `.strip()` removes whitespace (spaces, `\n`, tabs) from both ends of a string

---

## 3. Appending to a File

Adds to the **end** of the file without erasing what's already there.

```python
with open("hello.txt", "a") as file:
    file.write("This is a new line.\n")
```

- `"a"` — append mode
- If the file doesn't exist, it creates it (just like "w")
- If the file exists, it adds to the end (unlike "w" which erases first)

Example:
```python
# First run — creates file with one line
with open("log.txt", "a") as file:
    file.write("Entry 1\n")

# Second run — adds another line
with open("log.txt", "a") as file:
    file.write("Entry 2\n")
```

After both runs, log.txt contains:
```
Entry 1
Entry 2
```

If you used `"w"` instead of `"a"`, the file would only have "Entry 2" because `"w"` erases first.

---

## 4. File Modes Summary

| Mode  | Meaning | Creates file? | Erases existing? | Use when...                    |
|-------|---------|---------------|------------------|--------------------------------|
| `"r"` | Read    | No            | No               | You want to read a file        |
| `"w"` | Write   | Yes           | Yes              | You want to start fresh        |
| `"a"` | Append  | Yes           | No               | You want to add to existing    |

---

## 5. Why use `with`?

Files need to be **closed** after you're done with them. `with` does this automatically.

```python
# Without with (not recommended):
file = open("hello.txt", "r")
content = file.read()
file.close()    # easy to forget! If you forget, it can cause problems

# With with (recommended — always use this):
with open("hello.txt", "r") as file:
    content = file.read()
# file is automatically closed here, even if an error happens
```

Always use `with` — it's safer and cleaner.

---

## 6. Where does the file go?

The file is created in the **same folder** where you run your Python script.

If you run:
```bash
python3 ~/work/python/04_basic_io/exercises.py
```

Then files like "hello.txt" will be created in whatever directory your terminal is currently in (check with `pwd`).

To be safe, you can use a full path:
```python
with open("/home/p001955/work/python/04_basic_io/hello.txt", "w") as file:
    file.write("Hello!\n")
```

---

## 7. Checking if a File Exists

Before reading a file, you might want to check if it exists first (to avoid errors):

```python
import os

if os.path.exists("hello.txt"):
    print("File exists!")
else:
    print("File not found.")
```

- `import os` — loads the `os` module (a built-in toolbox for working with your operating system)
- `os.path.exists(...)` — returns True if the file exists, False if not
- We'll learn more about `import` later

---

## 8. Practical Example: Simple Note Taker

This combines writing, appending, and reading:

```python
# Write notes to a file (append so we don't erase old notes)
with open("notes.txt", "a") as file:
    while True:
        note = input("Enter a note (or 'quit' to stop): ")
        if note == "quit":
            break
        file.write(note + "\n")

# Read and display all notes
print("\nYour notes:")
with open("notes.txt", "r") as file:
    for line in file:
        print(line, end="")
```

What this does:
1. Opens "notes.txt" in append mode
2. Keeps asking for notes until user types "quit"
3. Writes each note to the file
4. After quitting, reads and displays all notes
