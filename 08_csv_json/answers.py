# CSV and JSON Answers — try solving them yourself first!

import csv
import json

# Exercise 1: Read CSV
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} lives in {row['city']}")

# Exercise 2: CSV Stats
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    people = list(reader)
    count = len(people)
    total_age = sum(int(p["age"]) for p in people)
    oldest = max(people, key=lambda p: int(p["age"]))
    print(f"Total people: {count}")
    print(f"Average age: {total_age / count:.1f}")
    print(f"Oldest: {oldest['name']}, age {oldest['age']}")

# Exercise 3: Write CSV
data = [
    ["name", "math", "science", "english"],
    ["Alice", 90, 85, 78],
    ["Bob", 72, 91, 88],
    ["Charlie", 85, 79, 92],
]

with open("scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

with open("scores.csv", "r") as file:
    print(file.read())

# Exercise 4: Read JSON
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data["students"]:
        status = "pass" if student["grade"] >= 70 else "fail"
        print(f"{student['name']} - {student['grade']} - {status}")

# Exercise 5: Write JSON
profile = {
    "name": "Dan",
    "age": 24,
    "hobbies": ["coding", "gaming", "reading"],
    "favorite_foods": ["pizza", "sushi", "ramen"]
}

with open("my_profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("my_profile.json", "r") as file:
    data = json.load(file)
    for key, value in data.items():
        print(f"{key}: {value}")

# Exercise 6: CSV to JSON Converter
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    people = list(reader)

with open("people.json", "w") as file:
    json.dump(people, file, indent=4)

print("Converted! Contents:")
with open("people.json", "r") as file:
    print(file.read())
