# CSV and JSON Exercises

# ============================================
# Exercise 1: Read CSV
# Read "people.csv" and print each person's
# name and city in this format:
#   Alice lives in New York
#   Bob lives in London
#   ...
# Use csv.DictReader.
# ============================================

# Write your code below:

# import csv

# with open("people.csv", "r") as file:
#     content = csv.DictReader(file)
#     for row in content:
#         print(f"{row['name']} lives in {row['city']}")



# ============================================
# Exercise 2: CSV Stats
# Read "people.csv" and:
#   - Print how many people are in the file
#   - Print the average age
#   - Print the oldest person's name and age
# ============================================

# # Write your code below:
# import csv

# with open("people.csv", "r") as file:
#     content = csv.DictReader(file)
#     people = list(content)
#     print(len(people))
#     ages = [int(person['age']) for person in people]
#     add = sum(ages)
#     print(add / len(people))
    
#     for row in content:
#         print(f"{row['name']} {row[max.(age)]}")

# ============================================
# Exercise 3: Write CSV
# Create a CSV file called "scores.csv" with this data:
#   name, math, science, english
#   Alice, 90, 85, 78
#   Bob, 72, 91, 88
#   Charlie, 85, 79, 92
# Then read it back and print it.
# ============================================

# Write your code below:

# import csv

# data = [{"name": "Alice", "math": "90", "science": "85", "english": "78"},
#     {"name": "Bob", "math": "72", "science": "91", "english": "88"}, 
#     {"name": "Charlie", "math": "85", "science": "79", "english": "92"}]

# with open("scores.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "math", "science", "english"])
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)
# with open("scores.csv", "r") as file:
#     content = csv.DictReader(file)
#     for row in content:
#         print(row)


# ============================================
# Exercise 4: Read JSON
# Read "students.json" and print each student's
# name and grade. Also print "pass" if grade >= 70,
# "fail" otherwise.
# Example: Alice - 90 - pass
# ============================================

# Write your code below:
# import json

# with open("students.json", "r") as file:
#     content = json.load(file)
#     for student in content["students"]:
#         name = student['name']
#         grade = student['grade']
#         status = "pass" if grade >= 70 else "fail"
#         print(f"{name} - {grade} - {status}")



# ============================================
# Exercise 5: Write JSON
# Create a dictionary with your personal info:
#   name, age, hobbies (list), favorite_foods (list)
# Save it to "my_profile.json" with pretty formatting.
# Then read it back and print each field.
# ============================================

# Write your code below:

# import json

# profile = {"name": "dan", "age": "24", "hobbies": ['play', 'watch', 'sleep'], "favorite_foods": ['burger', 'pizza', 'fried']}

# with open("my_profile.json", "w") as file:
#     json.dump(profile, file, indent = 4)
# with open("my_profile.json", "r") as file: 
#     content = json.load(file)
#     for key, value in content.items(): 
#         print(f"{key}: {value}")


# ============================================
# Exercise 6: CSV to JSON Converter
# Read "people.csv" and convert it to a JSON file
# called "people.json".
# The JSON should be a list of dictionaries.
# Example:
# [t
#     {"name": "Alice", "age": "30", "city": "New York"},
#     ...
# ]
# ============================================

# Write your code below:

# import csv
# import json

# with open("people.csv", "r") as file: 
#     content = csv.DictReader(file)
#     people = list(content)

# with open("people.json", "w") as file:
#     json.dump(people, file, indent = 4)

# with open("people.json", "r") as file:
#     content = json.load(file)
#     for person in content:
#         print(person)