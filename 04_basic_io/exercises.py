# Basic I/O Exercises

# ============================================
# Exercise 1: Write a File
# Create a file called "my_info.txt" and write
# 3 lines to it:
#   Your name
#   Your age
#   Your favorite color
# Then read the file and print its contents.
# ============================================

# # Write your code below:

# with open("my_info.txt", "w") as file:
#     file.write("Dan Mark\n")
#     file.write("24\n")
#     file.write("Olive Green\n")

# with open("my_info.txt", "r") as file:
#     content = file.read()
#     print(content)

# ============================================
# Exercise 2: Shopping List
# Ask the user to enter items one at a time.
# When they type "done", stop asking.
# Save all items to a file called "shopping.txt"
# with each item on its own line.
# Then read and print the file.
# ============================================

# # Write your code below:

# with open("shopping.txt", "w") as file:
#     while True:
#         item = input("Enter items one at a time, type done once finished:")
#         if item == "done":
#             break
#         file.write(item + "\n")

# with open("shopping.txt", "r") as file:
#     content = file.read()
#     print(content)





# ============================================
# Exercise 3: Line Counter
# Read the file "shopping.txt" (from Exercise 2)
# and print how many lines it has.
# Hint: use readlines() and len()
# ============================================

# # Write your code below:

# with open("shopping.txt", "r") as file:
#     content = file.readlines()
#     print(len(content))


# ============================================
# Exercise 4: Append to File
# Ask the user for one more shopping item.
# Append it to "shopping.txt" (don't erase
# the existing items).
# Then read and print the full file.
# ============================================

# Write your code below:

# with open("shopping.txt", "a") as file:
#     item = input("Add more items: ")
#     file.write(item + "\n")

# ============================================
# Exercise 5: File Copier
# Read the contents of "shopping.txt" and
# write them to a new file called "backup.txt".
# Print "Backup created!" when done.
# ============================================

# Write your code below:

# with open("shopping.txt", "r") as file:
#     content = file.read()
# with open("backup.txt", "w") as file:
#     file.write(content)
# print("Backup created!")


# ============================================
# Exercise 6: Simple Diary
# Create a program that:
# 1. Asks the user to type a diary entry
# 2. Appends it to "diary.txt" with today's date
# 3. Then shows all past entries
#
# For the date, use:
#   from datetime import date
#   today = str(date.today())
#
# Format in file:
#   [2026-04-10] This is my diary entry.
# ============================================

# Write your code below:

from datetime import date

note = input("Write your entry: ")
today = str(date.today())

with open("diary.txt", "a") as file:
    file.write(f"[{today}] {note}\n")

with open("diary.txt", "r") as diary:
    content = diary.read()

print(content)

