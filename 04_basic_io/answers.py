# Basic I/O Answers — try solving them yourself first!

# Exercise 1: Write a File
with open("my_info.txt", "w") as file:
    file.write("Alice\n")
    file.write("25\n")
    file.write("Blue\n")

with open("my_info.txt", "r") as file:
    print(file.read())

# Exercise 2: Shopping List
with open("shopping.txt", "w") as file:
    while True:
        item = input("Enter an item (or 'done' to stop): ")
        if item == "done":
            break
        file.write(item + "\n")

print("\nYour shopping list:")
with open("shopping.txt", "r") as file:
    print(file.read())

# Exercise 3: Line Counter
with open("shopping.txt", "r") as file:
    lines = file.readlines()
    print(f"The file has {len(lines)} lines.")

# Exercise 4: Append to File
item = input("Enter one more item: ")
with open("shopping.txt", "a") as file:
    file.write(item + "\n")

print("\nUpdated shopping list:")
with open("shopping.txt", "r") as file:
    print(file.read())

# Exercise 5: File Copier
with open("shopping.txt", "r") as source:
    content = source.read()

with open("backup.txt", "w") as backup:
    backup.write(content)

print("Backup created!")

# Exercise 6: Simple Diary
from datetime import date

today = str(date.today())
entry = input("Write your diary entry: ")

with open("diary.txt", "a") as file:
    file.write(f"[{today}] {entry}\n")

print("\nAll diary entries:")
with open("diary.txt", "r") as file:
    print(file.read())
