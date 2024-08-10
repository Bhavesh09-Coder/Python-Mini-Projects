
## Simple Banking System:
import os

class SimpleBankingSystem:
    def __init__(self):
        self.account_file = "accounts.txt"

    def create_account(self):
        pin = input("Enter a new 4-digit PIN: ")
        if os.path.exists(f"{pin}.txt"):
            print("Account with this PIN already exists!")
        else:
            with open(f"{pin}.txt", "w") as f:
                f.write("0")
            print("Account created successfully!")

    def deposit_money(self):
        pin = input("Enter your PIN: ")
        if os.path.exists(f"{pin}.txt"):
            amount = float(input("Enter amount to deposit: "))
            with open(f"{pin}.txt", "r") as f:
                balance = float(f.read())
            balance += amount
            with open(f"{pin}.txt", "w") as f:
                f.write(str(balance))
            print(f"Deposited {amount} successfully! New balance is {balance}")
        else:
            print("Account does not exist!")

    def withdraw_money(self):
        pin = input("Enter your PIN: ")
        if os.path.exists(f"{pin}.txt"):
            amount = float(input("Enter amount to withdraw: "))
            with open(f"{pin}.txt", "r") as f:
                balance = float(f.read())
            if amount <= balance:
                balance -= amount
                with open(f"{pin}.txt", "w") as f:
                    f.write(str(balance))
                print(f"Withdrawn {amount} successfully! New balance is {balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Account does not exist!")

    def check_balance(self):
        pin = input("Enter your PIN: ")
        if os.path.exists(f"{pin}.txt"):
            with open(f"{pin}.txt", "r") as f:
                balance = float(f.read())
            print(f"Current balance is {balance}")
        else:
            print("Account does not exist!")

    def change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if os.path.exists(f"{old_pin}.txt"):
            new_pin = input("Enter your new 4-digit PIN: ")
            if os.path.exists(f"{new_pin}.txt"):
                print("New PIN already in use. Choose another.")
            else:
                os.rename(f"{old_pin}.txt", f"{new_pin}.txt")
                print("PIN changed successfully!")
        else:
            print("Account does not exist!")

    def main(self):
        while True:
            print("\n--- Simple Banking System ---")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Change PIN")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.withdraw_money()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.change_pin()
            elif choice == '6':
                print("Thank you for using the Simple Banking System!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = SimpleBankingSystem()
    system.main()
