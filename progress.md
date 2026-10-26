# Python Learning Progress

## Section 1: Fundamentals

### ✅ Data Types (completed before starting)
- Strings, lists, tuples, dicts, sets

### ✅ Control Flow — 2026-03-29
- if / elif / else
- for loops
- while loops
- break and continue
- Nested loops
- `range()` (start, stop, step)
- `input()` and `int()`
- f-strings
- `print(end="")`
- `for/else` pattern
- Completed 11 exercises (Round 1: 5, Round 2: 6)

### ✅ Functions — 2026-03-29 to 2026-04-01
- Defining functions with `def`
- Parameters and arguments
- `return` vs `print()`
- Default parameters
- Multiple return values (position-based)
- Scope (variables inside functions)
- String indexing (`word[i]`)
- String methods (`.isdigit()`, `.upper()`, `.startswith()`)
- Methods vs functions (dot notation)
- Reserved keywords (`pass`, `if`, `return`, etc.)
- `+=` with strings (concatenation)
- Completed 12 exercises (Round 1: 6, Round 2: 6)
### ✅ String Formatting — 2026-04-10
- f-strings with variables and expressions
- Format specifiers (:.2f, :,, :.0%)
- Alignment (<, >, ^) with width
- Multiline strings with triple quotes """
- enumerate() for index + value in loops
- Completed 6 exercises
### ✅ Basic I/O (file reading/writing) — 2026-04-12
- Writing files with `open("file", "w")`
- Reading files with `open("file", "r")`
- Appending with `open("file", "a")`
- `with` statement for auto-closing files
- `.read()`, `.readlines()`, `.write()`
- `.strip()` to remove `\n`
- `from datetime import date` and `date.today()`
- `timedelta` for date math
- Completed 6 exercises

## Section 2: Intermediate Core Concepts
### ✅ List/dict/set comprehensions — 2026-04-12
- List comprehensions `[x for x in list]`
- Filtering with `if` after `for`
- Transforming with `if/else` before `for`
- Dict comprehensions `{k: v for k, v in dict.items()}`
- Set comprehensions `{x for x in list}`
- `.items()`, `.keys()`, `.values()` for dicts
- Completed 7 exercises
### ✅ Error handling — 2026-04-13
- try / except for catching errors
- Catching specific errors (ValueError, ZeroDivisionError, etc.)
- else block (runs if no error)
- finally block (always runs)
- Getting error messages with `as e`
- `Exception` as catch-all
- Raising errors with `raise`
- Completed 6 exercises
### ✅ Modules and packages — 2026-04-14
- Importing modules (import, from...import, as)
- Built-in modules (math, random, os, string, datetime)
- Creating your own modules
- `if __name__ == "__main__"` pattern
- Packages (folders with __init__.py)
- pip for installing external packages
- dir() and help() to explore modules
- Completed 6 exercises
### ✅ Working with files (CSV, JSON, text) — 2026-04-19
- Reading/writing CSV with csv.reader, csv.writer
- csv.DictReader and csv.DictWriter for dict-based access
- Reading/writing JSON with json.load, json.dump
- json.loads/json.dumps for strings
- Converting CSV to JSON
- newline="" for CSV writing
- indent parameter for pretty JSON
- Completed 6 exercises
### ✅ Object-Oriented Programming — 2026-04-19 to 2026-04-26
- Classes, objects, __init__, self
- Parameters vs attributes
- Methods with their own parameters
- Inheritance, super(), overriding methods
- Polymorphism (same method name, different behavior)
- Composition (objects containing other objects)
- Encapsulation (_ convention for private)
- Abstraction (ABC, @abstractmethod)
- __str__ and other dunder methods
- Completed 9 exercises (6 + 3 abstraction)
### ✅ Iterators and generators — 2026-05-03
- iter() and next() — how iteration works behind the scenes
- Creating custom iterators with __iter__ and __next__
- StopIteration to end iteration
- Generator functions with yield
- yield vs return (pause vs stop)
- Generator expressions (x for x in list)
- Memory efficiency of generators vs lists
- Completed 6 exercises
### ⬜ Decorators
### ⬜ Lambda functions, map, filter, reduce

## Section 3: Standard Library Deep Dive
### ⬜ os, sys, pathlib
### ⬜ datetime
### ⬜ collections
### ⬜ itertools, functools
### ⬜ re (regular expressions)
### ⬜ logging
### ⬜ unittest / pytest

## Section 4: Practical Project Skills
### ⬜ Virtual environments
### ⬜ Git
### ⬜ Debugging
### ⬜ Code style (PEP 8)
### ⬜ Type hints

## Section 5: Specialization
### ⬜ TBD — choose a track

## Section 6: Advanced Topics
### ⬜ Concurrency
### ⬜ Design patterns
### ⬜ Metaclasses and descriptors
### ⬜ Context managers
### ⬜ Performance profiling
### ⬜ Packaging
