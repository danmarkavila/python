# Functions Exercises - Round 2

# ============================================
# Exercise 1: Temperature Converter
# Create a function called "to_celsius" that takes
# a Fahrenheit temperature and RETURNS the Celsius value.
# Formula: (fahrenheit - 32) * 5 / 9
# Test it: to_celsius(100) should return 37.77...
# ============================================

# Write your code below:

def to_celsius(fahrenheit):
    result = (fahrenheit - 32) * 5 / 9
    return result

print(to_celsius(100))

# ============================================
# Exercise 2: Count Vowels
# Create a function called "count_vowels" that takes
# a string and RETURNS how many vowels (a, e, i, o, u) it has.
# Hint: use a for loop to go through each letter
# Test it: count_vowels("hello") should return 2
# ============================================

# Write your code below:

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count += 1
    return count
    
print(count_vowels("philippines"))



# ============================================
# Exercise 3: Reverse String
# Create a function called "reverse" that takes
# a string and RETURNS it reversed.
# Don't use any built-in reverse functions.
# Hint: build a new string by looping backwards
# Test it: reverse("hello") should return "olleh"
# ============================================

# Write your code below:

def reverse(word):
    reverse_word = ""
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]
    return reverse_word

print(reverse("philippines"))
    


# ============================================
# Exercise 4: Power Function
# Create a function called "power" that takes
# a base and an exponent (default exponent = 2).
# RETURN base raised to the exponent.
# Don't use ** or pow().
# Hint: use a loop to multiply
# Test it: power(3) → 9, power(2, 4) → 16
# ============================================

# Write your code below:

def power(base, exponent = 2):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(5))
print(power(3, 3))



# ============================================
# Exercise 5: Password Validator
# Create a function called "is_valid_password" that
# takes a password string and RETURNS True if:
#   - It is at least 8 characters long
#   - It contains at least one number
# Return False otherwise.
# Hint: use len() and loop through characters,
#       use .isdigit() to check if a character is a number
# ============================================

# Write your code below:

def is_valid_password(password):
    if len(password) < 8:
        return False
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    return has_number
    
print(is_valid_password("dan123dan"))






# ============================================
# Exercise 6: Mini ATM
# Create 3 functions:
#   - deposit(balance, amount) → returns new balance
#   - withdraw(balance, amount) → returns new balance
#     (but print "Insufficient funds" if amount > balance
#      and return the original balance)
#   - check_balance(balance) → prints the balance
#
# Then use a while loop to let the user choose:
#   1. Deposit  2. Withdraw  3. Check Balance  4. Exit
# Start with balance = 0
# ============================================

# Write your code below:
# // pass by reference
# // balance = 0
# // deposit(balanceArg = balance, amount)
# // deposit(balance, amount)
# // pass by value
# // balance = 0
# // deposit(balanceArg = balance, amount)
# // deposit(0, amount)

def deposit(balance, amount):
    return balance + amount
    

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
        return 
    return balance - amount

def check_balance(balance, amount):
    return balance
    
balance = 0
while True:
    print("\n1. Deposit 2. Withdraw 3. Check Balance 4. Exit")
    
    choice = input("Please choose a method: ")
    
    if choice == "1":
        amount = int(input("Please enter amount: "))
        balance = deposit(balance, amount)
    
    elif choice == "2":
        amount = int(input("Please enter amount: "))
        balance = withdraw(balance, amount)
    elif choice == "3":
         check_balance(balance, amount)
         print(f"Your balance is: {balance}")
    elif choice == "4":
        break