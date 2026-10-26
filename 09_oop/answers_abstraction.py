# Abstraction Answers — try solving them yourself first!

from abc import ABC, abstractmethod

# Exercise 1: Animal Sounds
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def info(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()
dog.info()
cat.speak()
cat.info()


# Exercise 2: Payment System
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def get_name(self):
        pass

class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        last_four = self.card_number[-4:]
        print(f"Paid ${amount} with credit card ending in {last_four}")

    def get_name(self):
        return "Credit Card"

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} in cash")

    def get_name(self):
        return "Cash"

payments = [CreditCard("1234567890123456"), Cash()]
for p in payments:
    print(f"Payment type: {p.get_name()}")
    p.pay(50)


# Exercise 3: Shape Calculator
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")

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

shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 5, 5, 4)]
for shape in shapes:
    shape.describe()
