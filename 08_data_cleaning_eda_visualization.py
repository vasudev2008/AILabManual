# Experiment 8: Data Cleaning, EDA and Visualization Using Pandas and Matplotlib
# Supplementary implementation based on the Experiment 8 title in the manual index.
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82],
}
df = pd.DataFrame(data)

print("--- Missing Values ---")
print(df.isnull().sum())
for column in ["Attendance", "Mark"]:
    df[column] = df[column].fillna(df[column].mean())
df = df.drop_duplicates()

print("\\n--- Cleaned Data ---")
print(df)
print("\\n--- Summary ---")
print(df.describe())

department_average = df.groupby("Department")["Mark"].mean()
department_average.plot(kind="bar", title="Department-wise Average Marks",
                        xlabel="Department", ylabel="Average Mark")
plt.tight_layout()
plt.savefig("experiment08_department_average.png")
plt.show()

df.plot(x="Name", y=["Mark", "Attendance"], kind="bar",
        title="Student Marks and Attendance")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("experiment08_student_comparison.png")
plt.show()
