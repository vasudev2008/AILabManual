# Experiment 1: Student Marks, Percentage, Grade and Academic Performance
name = input("Enter student name: ").strip()
n = int(input("Enter number of subjects: "))

if n <= 0:
    raise ValueError("Number of subjects must be positive.")

total = 0.0
for i in range(1, n + 1):
    mark = float(input(f"Enter mark for Subject {i}: "))
    if not 0 <= mark <= 100:
        raise ValueError("Each mark must be between 0 and 100.")
    total += mark

percentage = total / n

if percentage >= 90:
    grade, performance = "A+", "Outstanding"
elif percentage >= 80:
    grade, performance = "A", "Excellent"
elif percentage >= 70:
    grade, performance = "B", "Very Good"
elif percentage >= 60:
    grade, performance = "C", "Good"
elif percentage >= 50:
    grade, performance = "D", "Average"
else:
    grade, performance = "F", "Needs Improvement"

print("\\n--- Academic Performance ---")
print("Student Name :", name)
print("Total Marks  :", total)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)
print("Performance  :", performance)
