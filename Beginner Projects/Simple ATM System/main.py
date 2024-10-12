## Project title : Simple ATM System

def atm_system():
    balance = 1000
    pin = "1234"
    transaction_history = []

    entered_pin = input("Enter your PIN: ")
    if entered_pin != pin:
        print("Incorrect PIN!")
        return
    
    while True:
        action = input("Choose action (balance/withdraw/deposit/history/exit): ").lower()
        if action == 'balance':
            print(f"Your balance is: ${balance:.2f}")
        elif action == 'withdraw':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                transaction_history.append(f"Withdrew: ${amount:.2f}")
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
            else:
                print("Insufficient balance.")
        elif action == 'deposit':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Deposit successful. New balance: ${balance:.2f}")
        elif action == 'history':
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions found.")
        elif action == 'exit':
            print("Exiting ATM system.")
            break

atm_system()
