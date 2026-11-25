# Experiment 9: Data Visualization Using Matplotlib
# Supplementary implementation based on the Experiment 9 title in the manual index.
import matplotlib.pyplot as plt

students = ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"]
marks = [86, 91, 78, 88, 95]
attendance = [92, 85, 90, 88, 95]

# Bar chart
plt.figure()
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("experiment09_bar_chart.png")
plt.show()

# Line chart
plt.figure()
plt.plot(students, attendance, marker="o")
plt.title("Student Attendance")
plt.xlabel("Student")
plt.ylabel("Attendance (%)")
plt.tight_layout()
plt.savefig("experiment09_line_chart.png")
plt.show()

# Scatter plot
plt.figure()
plt.scatter(attendance, marks)
plt.title("Marks vs Attendance")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("experiment09_scatter_plot.png")
plt.show()

# Histogram
plt.figure()
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("experiment09_histogram.png")
plt.show()
