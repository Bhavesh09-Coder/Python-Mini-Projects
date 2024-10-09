import csv
import os

# File where data will be stored
file_name = 'data_entries.csv'

# Check if CSV exists, otherwise create it with headers
def initialize_csv():
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Email", "Phone", "Age"])

# Validate email format
def validate_email(email):
    return '@' in email and '.' in email

# Validate phone format (10 digits)
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Validate age
def validate_age(age):
    return age.isdigit() and 0 < int(age) < 120

# Add a new data entry
def add_entry():
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        user_id = input("Enter ID: ")
        name = input("Enter Name: ")

        # Email validation
        while True:
            email = input("Enter Email: ")
            if validate_email(email):
                break
            else:
                print("Invalid email format. Please try again.")

        # Phone validation
        while True:
            phone = input("Enter Phone (10 digits): ")
            if validate_phone(phone):
                break
            else:
                print("Invalid phone format. Please try again.")
        
        # Age validation
        while True:
            age = input("Enter Age: ")
            if validate_age(age):
                break
            else:
                print("Invalid age. Please enter a valid number.")
        
        writer.writerow([user_id, name, email, phone, age])
        print(f"Entry for {name} added successfully!")

# View all data entries
def view_entries():
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Edit an existing entry by ID
def edit_entry():
    user_id = input("Enter the ID of the entry to edit: ")
    rows = []

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    
    # Search for the entry by ID
    for i, row in enumerate(rows):
        if row[0] == user_id:
            print(f"Current Entry: {row}")
            rows[i][1] = input(f"Enter new name (Current: {row[1]}): ") or row[1]
            
            while True:
                email = input(f"Enter new email (Current: {row[2]}): ") or row[2]
                if validate_email(email):
                    rows[i][2] = email
                    break
                else:
                    print("Invalid email format. Please try again.")
            
            while True:
                phone = input(f"Enter new phone (Current: {row[3]}): ") or row[3]
                if validate_phone(phone):
                    rows[i][3] = phone
                    break
                else:
                    print("Invalid phone format. Please try again.")
            
            while True:
                age = input(f"Enter new age (Current: {row[4]}): ") or row[4]
                if validate_age(age):
                    rows[i][4] = age
                    break
                else:
                    print("Invalid age. Please enter a valid number.")
            print(f"Entry for ID {user_id} updated successfully!")
            break
    else:
        print(f"Entry with ID {user_id} not found.")

    # Overwrite the CSV with updated data
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Main menu to interact with the bot
def menu():
    while True:
        print("\n--- Data Entry Bot Menu ---")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Edit Existing Entry")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            edit_entry()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Initialize the CSV file and start the program
initialize_csv()
menu()
