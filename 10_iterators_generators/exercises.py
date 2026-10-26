# Iterators and Generators Exercises

# ============================================
# Exercise 1: Manual Iterator
# Use iter() and next() to manually loop through
# this list and print each item:
fruits = ["apple", "banana", "cherry"]
# Don't use a for loop!
# ============================================

# Write your code below:
# fruit = iter(fruits)
# 
# print(next(fruit))
# print(next(fruit))
# print(next(fruit))

# ============================================
# Exercise 2: Countdown Generator
# Create a generator function called "countdown"
# that takes a number and yields from that number
# down to 1, then yields "Go!"
# Example: countdown(3) → 3, 2, 1, Go!
# ============================================

# Write your code below:
# def countdown(number):
#     while number > 0:
#         yield number
#         number -= 1
#     yield "Go!"
# 
# num = countdown(5)
# for i in num:
#     print(i)
# ============================================
# Exercise 3: Fibonacci Generator
# Create a generator called "fibonacci" that takes
# a count and yields that many Fibonacci numbers.
# Fibonacci: each number is the sum of the previous two.
# Example: fibonacci(7) → 0, 1, 1, 2, 3, 5, 8
# ============================================

# Write your code below:
 #def fibonacci(count):
 #    a, b = 0, 1
 #    for i in range(count):
 #        yield a
 #        a, b = b, a + b
 #
 #for i in fibonacci(5):
 #    print(i)
# Use a generator expression to:
#   - Get only the odd numbers
#   - Square each one
#   - Print the sum of all squared odd numbers
# Do it in one line using sum() and a generator expression.
# ============================================

# Write your code below:

 #num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 #squared_odds = []
 #
 #for n in num:
 #    if n % 2 != 0:
 #        n **= 2
 #        squared_odds.append(n)
 #print(sum(squared_odds))
 #        
 #print(sum(n ** 2 for n in num if n % 2 != 0))
 #



# ============================================
# Exercise 5: File Word Counter
# Create a generator called "get_words" that:
#   - Takes a filename
#   - Reads the file line by line
#   - Yields each individual word (split by spaces)
#
# Then use it to count total words in "sample.txt"
# (Create sample.txt first with a few lines of text)
# ============================================

# Write your code below:

#
#def get_words(name):
#    with open(name, "r") as file:
#        for line in file:
#            for word in line.strip().split():
#                yield word
#
#
#count = 0
#for word in get_words("sample.txt"):
#    print(word)
#    count += 1
#print(f"Total words: {count}")


# ============================================
# Exercise 6: Custom Range
# Create an iterator CLASS called "MyRange" that
# works like range(start, end, step).
# It should have __iter__ and __next__ methods.
# Test it: for i in MyRange(0, 10, 2): print(i)
# Expected: 0, 2, 4, 6, 8
# ============================================

# Write your code below:


class MyRange:

    def __init__(self, start, end, step):
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




