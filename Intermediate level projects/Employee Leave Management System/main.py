import csv
import datetime

# File to store employee leave data
FILENAME = "employee_leaves.csv"

# Function to initialize the CSV file
def initialize_csv():
    """Initialize the CSV file if it doesn't exist."""
    try:
        with open(FILENAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Employee Name", "Leave Type", "From Date", "To Date", "Leave Status"])
    except FileExistsError:
        pass  # File already exists, no need to initialize

# Function to request leave
def request_leave(employee_name, leave_type, from_date, to_date):
    """Employee requests leave."""
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_name, leave_type, from_date, to_date, "Pending"])
    print(f"{employee_name} has requested {leave_type} leave from {from_date} to {to_date}.")

# Function to approve or reject leave
def manage_leave(employee_name, decision):
    """Manager approves or rejects leave."""
    rows = []
    leave_found = False
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == employee_name and row[4] == "Pending":
                leave_found = True
                if decision == "approve":
                    row[4] = "Approved"
                    print(f"Leave for {employee_name} has been approved.")
                elif decision == "reject":
                    row[4] = "Rejected"
                    print(f"Leave for {employee_name} has been rejected.")
            rows.append(row)

    if leave_found:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    else:
        print(f"No pending leave found for {employee_name}.")

# Function to view leave status for a particular employee
def view_leave_status(employee_name):
    """View leave status of an employee."""
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        print(f"Leave Status for {employee_name}:")
        found = False
        for row in reader:
            if row[0] == employee_name:
                print(f"Leave Type: {row[1]}, From: {row[2]}, To: {row[3]}, Status: {row[4]}")
                found = True
        if not found:
            print(f"No leave records found for {employee_name}.")

# Main program to demonstrate the leave management system
def main():
    initialize_csv()

    while True:
        print("\nEmployee Leave Management System")
        print("1. Request Leave")
        print("2. Manage Leave (Approve/Reject)")
        print("3. View Leave Status")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            leave_type = input("Enter leave type (Sick, Vacation, etc.): ")
            from_date = input("Enter leave start date (YYYY-MM-DD): ")
            to_date = input("Enter leave end date (YYYY-MM-DD): ")
            request_leave(name, leave_type, from_date, to_date)

        elif choice == "2":
            name = input("Enter employee name to manage leave: ")
            decision = input("Enter decision (approve/reject): ")
            manage_leave(name, decision)

        elif choice == "3":
            name = input("Enter employee name to view leave status: ")
            view_leave_status(name)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
