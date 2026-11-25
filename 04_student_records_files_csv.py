# Experiment 4: Student Record Management Using Lists, Tuples, Dictionaries, Files and CSV
import csv

students = [
    {"RollNo": "101", "Name": "Anitha", "Department": "CSE", "Mark": 86},
    {"RollNo": "102", "Name": "Bala", "Department": "CSE", "Mark": 91},
    {"RollNo": "103", "Name": "Chitra", "Department": "ECE", "Mark": 78},
]

# Tuple example: fixed course details
course = ("Python", 4)
print("Course Tuple:", course)

# Write records to a text file
with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(str(student) + "\\n")

# Write records to a CSV file
fields = ["RollNo", "Name", "Department", "Mark"]
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read and display the CSV file
print("\\n--- Records from CSV ---")
with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])
