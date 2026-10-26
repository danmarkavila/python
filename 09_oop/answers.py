# OOP Answers — try solving them yourself first!

# Exercise 1: Create a Person Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
p1.introduce()
p2.introduce()


# Exercise 2: Rectangle Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width} x {self.height})"

r = Rectangle(5, 3)
print(r.area())
print(r.perimeter())
print(r)


# Exercise 3: Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"{self.owner}'s account: ${self._balance}"

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)
acc.withdraw(200)
print(acc)


# Exercise 4: Inheritance — Vehicles
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def describe(self):
        print(f"{self.brand}, top speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):
        print(f"{self.brand}, top speed: {self.speed} km/h, {self.doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, brand, speed, moto_type):
        super().__init__(brand, speed)
        self.moto_type = moto_type

    def describe(self):
        print(f"{self.brand}, top speed: {self.speed} km/h, type: {self.moto_type}")

car = Car("Toyota", 180, 4)
moto = Motorcycle("Harley", 200, "cruiser")
car.describe()
moto.describe()


# Exercise 5: Todo List
class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def complete(self, index):
        try:
            removed = self.tasks.pop(index)
            print(f"Completed: {removed}")
        except IndexError:
            print("Invalid task number!")

    def show(self):
        if not self.tasks:
            print("No tasks!")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

todo = TodoList()
todo.add("Buy groceries")
todo.add("Clean house")
todo.add("Walk the dog")
todo.show()
todo.complete(0)
todo.show()


# Exercise 6: Student Roster
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

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if not self.students:
            return None
        best = self.students[0]
        for s in self.students:
            if s.average() > best.average():
                best = s
        return best

    def show_all(self):
        for s in self.students:
            print(s)

s1 = Student("Alice")
s1.add_grade(90)
s1.add_grade(85)

s2 = Student("Bob")
s2.add_grade(78)
s2.add_grade(92)

s3 = Student("Charlie")
s3.add_grade(95)
s3.add_grade(88)

room = Classroom()
room.add_student(s1)
room.add_student(s2)
room.add_student(s3)
room.show_all()
print(f"Top student: {room.top_student()}")
