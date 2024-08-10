## Expense Tracker:
class ExpenseTracker:
    def __init__(self):
        # Initialize an empty list to store expenses
        self.expenses = []

    def add_expense(self, description, amount):
        """
        Adds an expense to the tracker.

        :param description: A brief description of the expense
        :param amount: The amount spent on the expense
        """
        if amount <= 0:
            print("Amount should be greater than zero.")
            return
        
        # Append a tuple of description and amount to the expenses list
        self.expenses.append((description, amount))
        print(f"Added expense: {description} - ${amount}")

    def get_total_expenses(self):
        """
        Calculates and returns the total amount of all expenses.

        :return: Total amount of all expenses
        """
        total = sum(amount for description, amount in self.expenses)
        return total

    def display_expenses(self):
        """
        Displays all the expenses in a readable format.
        """
        print("Expense List:")
        for description, amount in self.expenses:
            print(f"{description}: ${amount}")
        print(f"Total Expenses: ${self.get_total_expenses()}")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter amount: "))
                tracker.add_expense(description, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            tracker.display_expenses()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
 
