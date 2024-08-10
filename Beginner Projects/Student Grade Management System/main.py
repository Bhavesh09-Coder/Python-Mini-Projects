"""
1. Student Grade Management System
Objective: Develop a system that manages student grades. It should allow users to add students with their grades, calculate the average grade, and determine the highest and lowest grades.

Requirements:

Use variables and data types to store student information and grades.
Implement type casting and type conversions for user inputs.
Utilize strings for student names.
Apply conditional statements to validate inputs and determine grade categories (e.g., A, B, C).
Use for loops and while loops to iterate through student data.
Create functions with arguments and keyword arguments to add students, calculate averages, and find the highest and lowest grades.
Optional: Use recursion to perform repeated grade calculations if needed.

"""
## Initialize an empty list to store student data

students = []

# Function to add a student
def add_student(name: str, grade: float):
    # Append a tuple of student name and grade to the list
    students.append((name, grade))

# Function to calculate average grade
def calculate_average():
    # Calculate the sum of all grades and divide by the number of students
    total = sum(grade for _, grade in students)
    average = total / len(students)
    return average

# Function to find the highest and lowest grades
def find_highest_lowest():
    # Find the highest and lowest grades using max and min functions
    highest = max(students, key=lambda student: student[1])
    lowest = min(students, key=lambda student: student[1])
    return highest, lowest

# Adding students (Example usage)
add_student("Alice", 88.5)
add_student("Bob", 92.0)
add_student("Charlie", 79.0)

# Calculate and print average grade
average = calculate_average()
print(f"Average Grade: {average}")

# Find and print highest and lowest grades
highest, lowest = find_highest_lowest()
print(f"Highest Grade: {highest[0]} with {highest[1]}")
print(f"Lowest Grade: {lowest[0]} with {lowest[1]}")
