# Importing the datetime module to work with dates
import datetime

# A dictionary to store friends' names and their birthdays
# The key is the friend's name, and the value is the birthday date in the format "YYYY-MM-DD"
birthdays = {
    "Alice": "1995-08-12",
    "Bob": "1990-03-16",
    "Charlie": "1985-05-25",
    "Diana": "2000-12-01"
}

# Function to check if today is someone's birthday
def check_birthday():
    # Get today's date in the format "YYYY-MM-DD"
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    
    # Initialize a variable to keep track of whether any birthdays are found
    birthday_found = False

    # Loop through the birthdays dictionary
    for name, bday in birthdays.items():
        # Compare the birthday date with today's date
        if bday[5:] == today[5:]:  # Only compare the month and day
            # If a birthday is found, print the name of the person
            print(f"Today is {name}'s birthday! Wish them a happy birthday!")
            birthday_found = True
    
    # If no birthdays are found, print a message
    if not birthday_found:
        print("No birthdays today.")

# Function to add a new birthday to the reminder
def add_birthday():
    # Ask the user for the friend's name
    name = input("Enter the friend's name: ")
    # Ask the user for the friend's birthday in the format "YYYY-MM-DD"
    bday = input("Enter the friend's birthday (YYYY-MM-DD): ")
    
    # Add the new entry to the birthdays dictionary
    birthdays[name] = bday
    print(f"Birthday for {name} added successfully!")

# Function to display all stored birthdays
def display_birthdays():
    print("Stored birthdays:")
    # Loop through the dictionary and print each entry
    for name, bday in birthdays.items():
        print(f"{name}: {bday}")

# Main function to run the birthday reminder program
def birthday_reminder():
    while True:
        # Display the menu options
        print("\nBirthday Reminder Menu:")
        print("1. Check today's birthdays")
        print("2. Add a new birthday")
        print("3. Display all birthdays")
        print("4. Exit")
        
        # Ask the user to choose an option
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            check_birthday()  # Check for today's birthdays
        elif choice == '2':
            add_birthday()  # Add a new birthday to the reminder
        elif choice == '3':
            display_birthdays()  # Display all stored birthdays
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

# Run the birthday reminder program
birthday_reminder()
