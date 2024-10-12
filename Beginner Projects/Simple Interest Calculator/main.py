def simple_interest(principal, rate, time):
    return principal * (rate / 100) * time

def compound_interest(principal, rate, time, times_compounded):
    return principal * (1 + rate / (100 * times_compounded)) ** (times_compounded * time)

def interest_calculator():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = int(input("Enter the time in years: "))
    
    interest_type = input("Simple or Compound Interest (S/C)? ").lower()
    
    if interest_type == 's':
        interest = simple_interest(principal, rate, time)
        print(f"Simple Interest: ${interest:.2f}")
    else:
        times_compounded = int(input("Enter the number of times interest is compounded per year: "))
        interest = compound_interest(principal, rate, time, times_compounded)
        print(f"Compound Interest: ${interest:.2f}")

interest_calculator()
