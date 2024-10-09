# Data Entry Bot

This project is a **Data Entry Bot** developed using Python. It automates the process of entering, storing, and managing data in a CSV file. The bot offers various advanced functionalities, such as data validation, viewing existing entries, and editing entries by ID. This project runs in a terminal or command-line environment, and all data is stored persistently in a CSV file.

## Features

- **Add New Entry**: Allows users to enter new data, including ID, name, email, phone number, and age, with validation for each field.
- **Email Validation**: Ensures that the email address follows a valid format.
- **Phone Number Validation**: Ensures that the phone number consists of 10 digits.
- **Age Validation**: Ensures that the age is a valid number between 0 and 120.
- **View Entries**: Displays all current entries stored in the CSV file in a readable format.
- **Edit Entry**: Updates an existing entry by its ID, allowing the user to modify the name, email, phone number, or age.
- **Persistent Storage**: Uses a CSV file to store data, which is saved across program executions.

## How It Works

1. **Main Menu**: The bot presents the user with a menu to choose from several options: add a new entry, view entries, edit an existing entry, or exit the program.
2. **Data Validation**: Before storing the data, the bot checks for valid input for emails, phone numbers, and ages, preventing incorrect data from being entered.
3. **Data Storage**: The entries are saved in a file named `data_entries.csv` in the current working directory, making the data persistent across different runs of the program.
4. **Edit Functionality**: Users can edit the fields of an entry by entering its unique ID. The bot will update the data in the CSV file.

## Requirements

- Python 3.x
- No external libraries are required; the script uses Python's standard libraries (csv, os).

## Running the Project

1. Clone or download this repository.
2. Run the `main.py` file using Python:
   ```bash
   python main.py
