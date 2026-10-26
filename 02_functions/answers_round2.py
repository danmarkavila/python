# Functions Round 2 Answers — try solving them yourself first!

# Exercise 1: Temperature Converter
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(to_celsius(100))    # 37.77...
print(to_celsius(32))     # 0.0

# Exercise 2: Count Vowels
def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("hello"))       # 2
print(count_vowels("python"))      # 1

# Exercise 3: Reverse String
def reverse(text):
    result = ""
    for char in text:
        result = char + result
    return result

print(reverse("hello"))    # olleh
print(reverse("python"))   # nohtyp

# Exercise 4: Power Function
def power(base, exponent=2):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(3))       # 9
print(power(2, 4))    # 16

# Exercise 5: Password Validator
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    return has_number

print(is_valid_password("hello"))          # False (too short)
print(is_valid_password("helloworld"))     # False (no number)
print(is_valid_password("hello123"))       # True

# Exercise 6: Mini ATM
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
        return balance
    return balance - amount

def check_balance(balance):
    print(f"Your balance is: {balance}")

balance = 0
while True:
    print("\n1. Deposit  2. Withdraw  3. Check Balance  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        balance = deposit(balance, amount)
    elif choice == "2":
        amount = int(input("Enter withdraw amount: "))
        balance = withdraw(balance, amount)
    elif choice == "3":
        check_balance(balance)
    elif choice == "4":
        print("Goodbye!")
        break
