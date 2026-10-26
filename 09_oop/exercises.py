# OOP Exercises

# ============================================
# Exercise 1: Create a Person Class
# Create a class called "Person" with:
#   - __init__ that takes name and age
#   - A method "introduce" that prints:
#     "Hi, I'm <name> and I'm <age> years old."
# Create 2 Person objects and call introduce on each.
# ============================================

# Write your code below:

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# p1 = Person("Dan", 24)
# p2 = Person("Mark", 23)

# p1.introduce()
# p2.introduce()


# ============================================
# Exercise 2: Rectangle Class
# Create a class called "Rectangle" with:
#   - __init__ that takes width and height
#   - A method "area" that returns width * height
#   - A method "perimeter" that returns 2 * (width + height)
#   - A __str__ method that returns "Rectangle(width x height)"
# Create a rectangle and print its area, perimeter, and the object.
# ============================================

# Write your code below:

# class Rectangle:

#     def __init__(self, width, height):
#         self.my_width = width
#         self.my_height = height
    
#     def area(self):
#         return self.my_width * self.my_height
    
#     def perimeter(self):
#         return 2 * (self.my_width + self.my_height)

#     def __str__(self):
#         return f"Rectangle {self.my_width} x {self.my_height}"
    
# rec1 = Rectangle(10, 20)

# print(rec1.area())
# print(rec1.perimeter())
# print(rec1)



# ============================================
# Exercise 3: Bank Account
# Create a class called "BankAccount" with:
#   - __init__ that takes owner and starting balance (default 0)
#   - A method "deposit" that adds money
#   - A method "withdraw" that removes money
#     (print "Insufficient funds" if not enough)
#   - A method "get_balance" that returns the balance
#   - A __str__ method: "<owner>'s account: $<balance>"
# Test it with deposits and withdrawals.
# ============================================

# Write your code below:

# class BankAccount:

#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self._balance = balance
    
#     def deposit(self, money):
#         self._balance += money
        
#     def withdraw(self, money):
#         if money > self._balance:
#             print("Insufficient funds")
#         else:    
#             self._balance -= money
        
#     def get_balance(self):
#         return self._balance
    
#     def __str__(self):
#         return f"{self.owner}'s account: ${self.get_balance()}"

# p1 = BankAccount("Dan")
# p1.deposit(50)
# p1.withdraw(40)
# print(p1)


# ============================================
# Exercise 4: Inheritance — Vehicles
# Create a base class "Vehicle" with:
#   - __init__ that takes brand and speed
#   - A method "describe" that prints brand and speed
#
# Create two child classes:
#   - "Car" that adds a "doors" attribute
#   - "Motorcycle" that adds a "type" attribute (sport, cruiser, etc.)
# Both should override "describe" to include their extra info.
# Use super() in __init__.
# ============================================

# Write your code below:


# class Vehicle:

#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#     def describe(self):
#         print(f"{self.brand} with {self.speed} miles per hour")

# class Car(Vehicle):

#     def __init__(self, branch, speed, doors):
#         super().__init__(branch, speed)
#         self.doors = doors

#     def describe(self):
#         print(f"{self.brand} with {self.speed} miles per hour with {self.doors}")

# class Motorcycle(Vehicle):
#     def __init__(self, branch, speed, moto_type):
#         super().__init__(branch, speed)
#         self.moto_type = moto_type

#     def describe(self):
#         print(f"{self.brand} with {self.speed} miles per hour of {self.moto_type}")

# car1 = Car("Toyota", 400, 4)
# car1.describe()

# moto1 = Motorcycle("Harley", 200, "cruiser")
# moto1.describe()


# ============================================
# Exercise 5: Todo List
# Create a class called "TodoList" with:
#   - __init__ that creates an empty list of tasks
#   - A method "add" that takes a task string and adds it
#   - A method "complete" that takes an index and removes that task
#     (handle invalid index with try/except)
#   - A method "show" that prints all tasks with numbers:
#     1. Buy groceries
#     2. Clean house
# Test it by adding, completing, and showing tasks.
# ============================================

# Write your code below:

# class TodoList:
#     def __init__(self):
#         self.task = []

#     def add(self, task):
#         self.task.append(task)

#     def complete(self, index):
#         try:
#             self.task.pop(index)
#         except IndexError:
#             print("Invalid task number!")

#     def show(self):
#         for i, task in enumerate(self.task):
#             print(f"{i + 1}. {task}")

# todo = TodoList()
# todo.add("Review")
# todo.add("Study")
# todo.show()
# todo.complete(0)
# todo.show()
# todo.complete(5)
# todo.show()


# ============================================
# Exercise 6: Student Roster
# Create a "Student" class with:
#   - name and a list of grades
#   - A method "add_grade"
#   - A method "average" that returns the average grade
#   - A __str__ that shows name and average
#
# Create a "Classroom" class with:
#   - A list of students
#   - A method "add_student" that takes a Student
#   - A method "top_student" that returns the student
#     with the highest average
#   - A method "show_all" that prints all students
# ============================================

# Write your code below:

class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grades):
        self.grades.append(grades)
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"{self.name} with grade {self.grades}"
class Classroom:
    def __init__(self):
        self.students = []
    def add_students(self, student):
        self.students.append(student)
    def top_student(self):
        best = self.students[0]
        for student in self.students:
            if student.average() > best.average():
                best = student
        return best
    def show_all(self):
        for student in self.students:
            print(student)


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
room.add_students(s1)
room.add_students(s2)
room.add_students(s3)

room.show_all()
print(f"Top student: {room.top_student()}")