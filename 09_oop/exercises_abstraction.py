# Abstraction Exercises

from abc import ABC, abstractmethod

# ============================================
# Exercise 1: Animal Sounds
# Create an abstract class "Animal" with:
#   - __init__ that takes name
#   - An abstract method "speak"
#   - A regular method "info" that prints the name
#
# Create two child classes:
#   - "Dog" that implements speak → "<name> says Woof!"
#   - "Cat" that implements speak → "<name> says Meow!"
# Create objects and call speak and info on each.
# ============================================

# Write your code below:

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def speak(self):
#         pass

#     def info(self):
#         print(f"Name: {self.name}")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says Woof!")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says Meow!")

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# dog.info()
# dog.speak()
# cat.info()
# cat.speak()



# ============================================
# Exercise 2: Payment System
# Create an abstract class "Payment" with:
#   - An abstract method "pay" that takes an amount
#   - An abstract method "get_name" that returns the payment type
#
# Create two child classes:
#   - "CreditCard" with a card_number attribute
#     pay prints: "Paid $<amount> with credit card ending in <last 4 digits>"
#   - "Cash"
#     pay prints: "Paid $<amount> in cash"
#
# Test both with a list of payments.
# ============================================

# Write your code below:

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass
    
#     @abstractmethod
#     def get_name(self):
#         pass

# class CreditCard(Payment):
#     def __init__(self, card_number):
#         self.card_number = card_number

#     def pay(self, amount):
#         print(f"Paid ${amount} with credit card ending in {self.card_number[-4:]}")

#     def get_name(self):
#         return "Credit Card"
    
# class Cash(Payment):
#     def pay(self, amount):
#         print(f"Paid ${amount} in cash")

#     def get_name(self):
#         return "Cash"
# payments = [CreditCard("1234567890123456"), Cash()]
# for p in payments:
#     print(f"Payment type: {p.get_name()}")
#     p.pay(50)

# ============================================
# Exercise 3: Shape Calculator
# Create an abstract class "Shape" with:
#   - Abstract methods: area() and perimeter()
#   - A regular method "describe" that prints:
#     "Area: <area>, Perimeter: <perimeter>"
#
# Create three child classes:
#   - Rectangle (width, height)
#   - Circle (radius) — use 3.14159 for pi
#   - Triangle (a, b, c for sides, and height)
#     area = 0.5 * base(a) * height
#     perimeter = a + b + c
#
# Create a list of shapes and call describe on each.
# ============================================

# Write your code below:

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c
    

shapes = [Rectangle(4, 5), Circle(3), Triangle(3, 4, 5, 2)]
for shape in shapes:
    shape.describe()
    