
## Text-Based Loan Calculator:
import math

def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly payment for a loan.
    
    :param principal: The loan amount (principal).
    :param annual_interest_rate: The annual interest rate (as a percentage).
    :param years: The number of years to repay the loan.
    :return: The monthly payment amount.
    """
    monthly_interest_rate = annual_interest_rate / 100 / 12  # Convert annual rate to monthly and percentage to decimal
    number_of_payments = years * 12  # Total number of monthly payments

    if monthly_interest_rate == 0:  # Special case for zero interest rate
        return principal / number_of_payments

    # Formula to calculate the monthly payment
    monthly_payment = principal * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, number_of_payments)) / (math.pow(1 + monthly_interest_rate, number_of_payments) - 1)
    return monthly_payment

def calculate_repayment_schedule(principal, annual_interest_rate, years):
    """
    Calculate the full repayment schedule for a loan.
    
    :param principal: The loan amount (principal).
    :param annual_interest_rate: The annual interest rate (as a percentage).
    :param years: The number of years to repay the loan.
    :return: A list of dictionaries representing the repayment schedule.
    """
    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    balance = principal
    schedule = []

    for month in range(1, years * 12 + 1):
        interest_payment = balance * (annual_interest_rate / 100 / 12)
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        schedule.append({
            'Month': month,
            'Interest Payment': round(interest_payment, 2),
            'Principal Payment': round(principal_payment, 2),
            'Remaining Balance': round(balance, 2)
        })

    return schedule

def display_schedule(schedule):
    """
    Display the repayment schedule in a readable format.
    
    :param schedule: The repayment schedule as a list of dictionaries.
    """
    print("{:<10} {:<20} {:<20} {:<20}".format('Month', 'Interest Payment', 'Principal Payment', 'Remaining Balance'))
    for payment in schedule:
        print("{:<10} {:<20} {:<20} {:<20}".format(payment['Month'], payment['Interest Payment'], payment['Principal Payment'], payment['Remaining Balance']))

def main():
    """
    Main function to run the loan calculator.
    """
    print("Welcome to the Loan Repayment Calculator")
    principal = float(input("Enter the loan amount (principal): "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the number of years to repay the loan: "))

    monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
    print(f"\nYour monthly payment will be: ${round(monthly_payment, 2)}")

    schedule = calculate_repayment_schedule(principal, annual_interest_rate, years)
    print("\nRepayment Schedule:")
    display_schedule(schedule)

if __name__ == "__main__":
    main()
