# A dictionary to store contacts where the key is the contact's name and the value is their phone number
phone_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    
    # Adding the new contact to the phone book
    phone_book[name] = phone
    print(f"Contact {name} added successfully.")

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name of the contact to search: ")
    
    # Check if the contact exists in the phone book
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact by name
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    # Check if the contact exists and delete it
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

# Function to edit a contact's phone number
def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    
    # Check if the contact exists
    if name in phone_book:
        new_phone = input("Enter the new phone number: ")
        phone_book[name] = new_phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

# Function to display all contacts
def display_contacts():
    if phone_book:
        print("All contacts:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts in phone book.")

# Function to save contacts to a plain text file
def save_contacts():
    with open('phone_book.txt', 'w') as file:
        for name, phone in phone_book.items():
            file.write(f"{name}: {phone}\n")
    print("Contacts saved successfully.")

# Function to load contacts from a plain text file
def load_contacts():
    global phone_book
    try:
        with open('phone_book.txt', 'r') as file:
            for line in file:
                name, phone = line.strip().split(": ")
                phone_book[name] = phone
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("No saved contacts found.")

# Main function to run the phone book application
def phone_book_app():
    load_contacts()
    
    while True:
        print("\nPhone Book Menu:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Edit contact")
        print("5. Display all contacts")
        print("6. Save contacts")
        print("7. Exit")
        
        choice = input("Choose an option (1/2/3/4/5/6/7): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            save_contacts()
        elif choice == '7':
            save_contacts()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phone book application
phone_book_app()
