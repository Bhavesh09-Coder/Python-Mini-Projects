# Project Title: Employee Attendance System

# Step 1: Create a dictionary to hold employee names and their attendance status
employee_attendance = {
    "John Doe": "Absent",
    "Jane Smith": "Absent",
    "Michael Brown": "Absent",
    "Emma Davis": "Absent",
    "Oliver Wilson": "Absent"
}

# Step 2: Function to mark attendance
def mark_attendance(employee_name):
    """
    Mark an employee's attendance as 'Present'.
    
    :param employee_name: Name of the employee
    """
    if employee_name in employee_attendance:
        employee_attendance[employee_name] = "Present"
        print(f"Attendance marked for {employee_name}.")
    else:
        print(f"Employee {employee_name} does not exist in the system.")

# Step 3: Function to display attendance record
def display_attendance():
    """
    Display the attendance record of all employees.
    """
    print("\nEmployee Attendance Record:")
    for employee, status in employee_attendance.items():
        print(f"{employee}: {status}")

# Step 4: Main menu loop for user interaction
def attendance_system():
    """
    Run the employee attendance system, allowing users to mark attendance or view records.
    """
    while True:
        print("\n--- Employee Attendance System ---")
        print("1. Mark Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the employee's name: ")
            mark_attendance(name)
        elif choice == '2':
            display_attendance()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Step 5: Run the attendance system
attendance_system()
