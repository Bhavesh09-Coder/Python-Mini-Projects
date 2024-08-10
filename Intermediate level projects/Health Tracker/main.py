
Health Tracker :
# Health Tracker Advanced

import datetime
import matplotlib.pyplot as plt

# Function to display the main menu
def display_menu():
    print("\nHealth Tracker Menu")
    print("1. Add a new entry")
    print("2. View entries")
    print("3. View summary statistics")
    print("4. Plot data trends")
    print("5. Exit")

# Function to validate date input
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to add a new entry
def add_entry():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    exercise = input("Enter exercise details: ")
    water_intake = input("Enter water intake (liters): ")
    sleep_hours = input("Enter sleep hours: ")
    calories = input("Enter calories consumed: ")
    mood = input("Enter your mood: ")

    # Save the entry to a file
    with open("health_tracker.txt", "a") as file:
        file.write(f"{date},{exercise},{water_intake},{sleep_hours},{calories},{mood}\n")
    print("Entry added successfully!")

# Function to view all entries
def view_entries():
    try:
        with open("health_tracker.txt", "r") as file:
            entries = file.readlines()
            if entries:
                print("\nDate       | Exercise           | Water Intake (L) | Sleep Hours | Calories | Mood")
                print("----------------------------------------------------------------------------")
                for entry in entries:
                    date, exercise, water_intake, sleep_hours, calories, mood = entry.strip().split(',')
                    print(f"{date} | {exercise} | {water_intake}          | {sleep_hours} | {calories} | {mood}")
            else:
                print("No entries found.")
    except FileNotFoundError:
        print("No entries found.")

# Function to view summary statistics
def view_summary_statistics():
    try:
        with open("health_tracker.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("No entries found.")
                return

            total_water = 0
            total_sleep = 0
            total_calories = 0
            entry_count = 0

            for entry in entries:
                _, _, water_intake, sleep_hours, calories, _ = entry.strip().split(',')
                total_water += float(water_intake)
                total_sleep += float(sleep_hours)
                total_calories += int(calories)
                entry_count += 1

            print("\nSummary Statistics:")
            print(f"Total entries: {entry_count}")
            print(f"Average water intake: {total_water / entry_count:.2f} liters")
            print(f"Average sleep hours: {total_sleep / entry_count:.2f} hours")
            print(f"Average calories consumed: {total_calories / entry_count:.2f} calories")
    except FileNotFoundError:
        print("No entries found.")

# Function to plot data trends
def plot_data_trends():
    try:
        with open("health_tracker.txt", "r") as file:
            entries = file.readlines()
            if not entries:
                print("No entries found.")
                return

            dates = []
            water_intakes = []
            sleep_hours = []
            calories = []

            for entry in entries:
                date, _, water_intake, sleep_hours, calories, _ = entry.strip().split(',')
                dates.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
                water_intakes.append(float(water_intake))
                sleep_hours.append(float(sleep_hours))
                calories.append(int(calories))

            plt.figure(figsize=(10, 6))
            
            plt.subplot(3, 1, 1)
            plt.plot(dates, water_intakes, marker='o', linestyle='-', color='b')
            plt.title('Water Intake Over Time')
            plt.xlabel('Date')
            plt.ylabel('Water Intake (L)')

            plt.subplot(3, 1, 2)
            plt.plot(dates, sleep_hours, marker='o', linestyle='-', color='g')
            plt.title('Sleep Hours Over Time')
            plt.xlabel('Date')
            plt.ylabel('Sleep Hours')

            plt.subplot(3, 1, 3)
            plt.plot(dates, calories, marker='o', linestyle='-', color='r')
            plt.title('Calories Consumed Over Time')
            plt.xlabel('Date')
            plt.ylabel('Calories')

            plt.tight_layout()
            plt.show()

    except FileNotFoundError:
        print("No entries found.")

# Main function to run the health tracker
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            view_summary_statistics()
        elif choice == "4":
            plot_data_trends()
        elif choice == "5":
            print("Exiting Health Tracker. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
