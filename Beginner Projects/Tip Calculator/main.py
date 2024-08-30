# Project Title: Tip Calculator

def tip_calculator():
    print("Welcome to the Tip Calculator!")

    # Get the bill amount from the user
    while True:
        try:
            bill_amount = float(input("Enter the total bill amount: $"))
            if bill_amount <= 0:
                print("Please enter a valid amount greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Get the desired tip percentage from the user
    while True:
        try:
            tip_percentage = int(input("Enter the tip percentage you'd like to give (e.g., 10, 15, 20): "))
            if tip_percentage < 0:
                print("Tip percentage cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid percentage.")

    # Get the number of people splitting the bill
    while True:
        try:
            num_people = int(input("Enter the number of people splitting the bill: "))
            if num_people <= 0:
                print("There must be at least one person to split the bill.")
            else:
                break
        except ValueError:
            print("Please enter a valid number of people.")

    # Calculate the tip amount
    tip_amount = (bill_amount * tip_percentage) / 100

    # Calculate the total amount (bill + tip)
    total_amount = bill_amount + tip_amount

    # Calculate the amount per person
    amount_per_person = total_amount / num_people

    # Display the results
    print(f"\nTip Amount: ${tip_amount:.2f}")
    print(f"Total Amount (including tip): ${total_amount:.2f}")
    print(f"Amount per person: ${amount_per_person:.2f}")

if __name__ == "__main__":
    tip_calculator()
