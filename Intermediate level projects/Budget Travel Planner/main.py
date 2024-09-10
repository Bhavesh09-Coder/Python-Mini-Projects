# Project Title: Budget Travel Planner

# Function to calculate daily budget
def calculate_daily_budget(total_budget, days):
    return total_budget / days

# Function to track expenses and check remaining budget
def track_expenses(total_budget, expenses):
    return total_budget - sum(expenses)

# Function to display the planner information
def travel_planner():
    print("Welcome to the Budget Travel Planner!")

    # Input the total travel budget and number of days
    total_budget = float(input("Enter your total travel budget ($): "))
    days = int(input("Enter the number of days you plan to travel: "))
    
    # Calculate daily budget
    daily_budget = calculate_daily_budget(total_budget, days)
    print(f"Your daily budget is: ${daily_budget:.2f}")

    # List to store expenses
    expenses = []

    # Loop to add daily expenses
    for day in range(1, days + 1):
        print(f"\nDay {day}:")

        # Input the daily expense for that day
        daily_expense = float(input("Enter your daily expense ($): "))
        expenses.append(daily_expense)

        # Check remaining budget
        remaining_budget = track_expenses(total_budget, expenses)
        print(f"Remaining budget: ${remaining_budget:.2f}")

        # Check if budget is exceeded
        if remaining_budget < 0:
            print(f"Warning: You have exceeded your budget by ${abs(remaining_budget):.2f}")
            break

    # Final summary
    total_expenses = sum(expenses)
    if total_expenses <= total_budget:
        print("\nCongratulations! You stayed within your budget.")
    else:
        print("\nYou exceeded your budget.")

    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Total remaining budget: ${total_budget - total_expenses:.2f}")

# Run the travel planner
travel_planner()
