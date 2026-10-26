# Object-Oriented Programming (OOP)

So far, you've been writing functions and variables separately.
OOP lets you bundle related data and functions together into one thing called a **class**.

---

## 1. What is a Class?

A class is a blueprint for creating objects. Think of it like a form — the class is the blank form, and each object is a filled-out form.

```python
class Dog:
    def __init__(self, n, a):
        self.dog_name = n
        self.dog_age = a

    def bark(self):
        print(f"{self.dog_name} says Woof!")

# Create objects (instances) from the class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.dog_name)    # Buddy
print(dog2.dog_age)     # 5
dog1.bark()              # Buddy says Woof!
dog2.bark()              # Max says Woof!
```

Let's break this down piece by piece.

---

## 2. The `__init__` Method

`__init__` is a special method that runs automatically when you create an object. It sets up the object's data.

```python
class Dog:
    def __init__(self, n, a):
        self.dog_name = n    # save n on the object as dog_name
        self.dog_age = a     # save a on the object as dog_age
```

- `__init__` = "initialize" — sets up the object
- It runs automatically when you do `Dog("Buddy", 3)`
- You never call `__init__` directly

There are two different things on each line:

```python
self.dog_name = n
#    ^^^^^^^^   ^
#    |          |
#    attribute  parameter
```

- **Parameter** (`n`) — the value coming in. It's temporary — disappears after `__init__` finishes.
- **Attribute** (`self.dog_name`) — where you save it on the object. It's permanent — stays on the object forever.
- `dog_name` has no relation to `dog1` — it's just a label you choose. Could be `self.xyz` or `self.banana`.

Without `self.dog_name = n`, the value "Buddy" arrives, gets used nowhere, and disappears:

```python
class Dog:
    def __init__(self, n, a):
        pass    # didn't save anything!

    def bark(self):
        print(self.dog_name)    # ERROR — dog_name was never saved

dog1 = Dog("Buddy", 3)
dog1.bark()    # crashes!
```

Here's what happens step by step when you create an object:

```python
dog1 = Dog("Buddy", 3)
```

1. Creates an empty object → `dog1`
2. Runs `__init__` automatically
3. `n` receives `"Buddy"`, `a` receives `3` (temporary)
4. `self.dog_name = n` → saves `"Buddy"` inside `dog1` as `dog_name`
5. `self.dog_age = a` → saves `3` inside `dog1` as `dog_age`
6. `__init__` finishes → `n` and `a` disappear
7. `dog1.dog_name` and `dog1.dog_age` are still there ✅

So `"Buddy"` and `3` are only saved in `dog1` because of the `self.dog_name = n` and `self.dog_age = a` lines. Without them, the object would be empty.

Whatever you put after `self.` becomes the way you access it later:

```python
# If you used self.dog_name:
print(dog1.dog_name)    # Buddy

# If you used self.banana instead:
print(dog1.banana)      # Buddy — same value, different label
```

**Note:** Most Python code uses the same name for both (like `self.name = name`). This is the convention, but it can be confusing when learning. They are still two different things — the parameter on the right brings the value in, the attribute on the left saves it.

### What is `self`?

`self` refers to the specific object being created. It's how the object talks about itself.

```python
dog1 = Dog("Buddy", 3)
# When this runs, inside __init__:
# self = dog1
# self.name = "Buddy"  →  dog1.name = "Buddy"
# self.age = 3         →  dog1.age = 3

dog2 = Dog("Max", 5)
# When this runs, inside __init__:
# self = dog2
# self.name = "Max"    →  dog2.name = "Max"
# self.age = 5         →  dog2.age = 5
```

- `self` is always the first parameter in every method
- You don't pass it when calling — Python does it automatically
- `self.name` means "this object's name"

---

## 3. Methods

Methods are functions that belong to a class. They can access the object's data through `self`.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age}!")

dog1 = Dog("Buddy", 3)
dog1.bark()        # Buddy says Woof!
dog1.birthday()    # Buddy is now 4!
dog1.birthday()    # Buddy is now 5!
print(dog1.age)    # 5
```

- Methods are just functions inside a class
- They always take `self` as the first parameter
- They can read and change the object's data

---

## 4. Attributes

Attributes are variables that belong to an object. You set them with `self.something`.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand      # attribute
        self.color = color      # attribute
        self.speed = 0          # attribute with default value

    def accelerate(self):
        self.speed += 10

car = Car("Toyota", "Red")
print(car.brand)    # Toyota
print(car.speed)    # 0
car.accelerate()
print(car.speed)    # 10
```

- Attributes set in `__init__` are available everywhere in the class
- You can also set default values (like `self.speed = 0`)

---

## 5. Inheritance

A class can inherit from another class — it gets all the parent's methods and attributes, and can add its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()    # Buddy says Woof!
cat.speak()    # Whiskers says Meow!
```

- `class Dog(Animal):` — Dog inherits from Animal
- Dog gets `__init__` and `name` from Animal automatically
- Dog **overrides** `speak()` with its own version
- This is called **polymorphism** — same method name, different behavior

### Using `super()` to call the parent:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # call Animal's __init__
        self.breed = breed        # add Dog-specific attribute

dog = Dog("Buddy", "Labrador")
print(dog.name)     # Buddy (from Animal)
print(dog.breed)    # Labrador (from Dog)
```

- `super()` calls the parent class's method
- Useful when you want to extend, not replace, the parent's behavior

---

## 6. Encapsulation

Encapsulation means keeping some data private — not meant to be accessed directly from outside.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance    # _ means "private, don't touch directly"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.get_balance())    # 150
```

- `_balance` — the underscore `_` is a convention meaning "this is private"
- Python doesn't actually prevent access, it's just a signal to other programmers
- Use methods like `deposit()` and `get_balance()` to interact with private data

---

## 7. The `__str__` Method

Controls what happens when you `print()` an object.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, age {self.age}"

dog = Dog("Buddy", 3)
print(dog)    # Buddy, age 3
```

Without `__str__`, printing an object shows something ugly like `<__main__.Dog object at 0x7f...>`.

---

## 8. Abstraction

Abstraction means defining a blueprint that says "any child class MUST have these methods" — without implementing them in the parent.

You use the `abc` module (Abstract Base Class):

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

- `ABC` — makes the class abstract
- `@abstractmethod` — marks a method that children MUST implement
- `pass` — the parent doesn't provide the actual code

Now if you try to create a Shape directly:

```python
s = Shape()    # ERROR! Can't create an abstract class
```

Children MUST implement all abstract methods:

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):                          # MUST implement this
        return self.width * self.height

    def perimeter(self):                     # MUST implement this
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                          # MUST implement this
        return 3.14159 * self.radius ** 2

    def perimeter(self):                     # MUST implement this
        return 2 * 3.14159 * self.radius
```

If a child forgets to implement a method:

```python
class Triangle(Shape):
    def area(self):
        return 10
    # forgot perimeter!

t = Triangle()    # ERROR! Can't create — perimeter is missing
```

### Why use abstraction?

It guarantees that all children have the same methods. This works perfectly with polymorphism:

```python
shapes = [Rectangle(5, 3), Circle(4), Rectangle(10, 2)]

for shape in shapes:
    print(f"Area: {shape.area()}")          # guaranteed to exist
    print(f"Perimeter: {shape.perimeter()}") # guaranteed to exist
```

Without abstraction, you'd have to trust that every child class remembered to add `area()` and `perimeter()`. With it, Python forces them to.

### The four pillars of OOP:

1. **Encapsulation** — hide data, use methods to access it (`self._balance`)
2. **Inheritance** — child gets everything from parent (`class Dog(Animal)`)
3. **Polymorphism** — same method name, different behavior per class
4. **Abstraction** — define required methods without implementing them

---

## 9. Composition — Objects Inside Objects

Composition is when one object **contains** other objects. This is different from inheritance (parent-child relationship).

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []    # will contain Student objects

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        best = self.students[0]
        for student in self.students:
            if student.average() > best.average():
                best = student
        return best
```

- `Student` and `Classroom` are independent classes — no inheritance
- The connection happens through **objects**, not classes
- You create Student objects, then put them inside a Classroom object

```python
s1 = Student("Alice")
s1.add_grade(90)

room = Classroom()
room.add_student(s1)    # Student object is now inside Classroom
room.top_student()      # Classroom uses Student's .average() method
```

Use **inheritance** when one thing IS another (Dog IS an Animal).
Use **composition** when one thing HAS another (Classroom HAS Students).

---

## 9. Practical Example: Student Grade Tracker

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}: avg {self.average():.1f}"

s = Student("Alice")
s.add_grade(90)
s.add_grade(85)
s.add_grade(92)
print(s)              # Alice: avg 89.0
print(s.grades)       # [90, 85, 92]
print(s.average())    # 89.0
```
