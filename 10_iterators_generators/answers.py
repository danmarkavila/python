# Iterators and Generators Answers — try solving them yourself first!

# Exercise 1: Manual Iterator
fruits = ["apple", "banana", "cherry"]
it = iter(fruits)
print(next(it))
print(next(it))
print(next(it))

# Exercise 2: Countdown Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Go!"

for item in countdown(3):
    print(item)

# Exercise 3: Fibonacci Generator
def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num)

# Exercise 4: Generator Expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(x ** 2 for x in numbers if x % 2 != 0))

# Exercise 5: File Word Counter
def get_words(filename):
    with open(filename, "r") as file:
        for line in file:
            for word in line.strip().split():
                yield word

count = 0
for word in get_words("sample.txt"):
    count += 1
print(f"Total words: {count}")

# Exercise 6: Custom Range
class MyRange:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for i in MyRange(0, 10, 2):
    print(i)
