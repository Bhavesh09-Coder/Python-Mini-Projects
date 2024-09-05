# Project Title : Personal Finance Manager

import datetime

class PersonalFinanceManager:
    def __init__(self):
        self.transactions = []
    
    def add_transaction(self, amount, category, date=None):
        if date is None:
            date = datetime.date.today()
        self.transactions.append({
            'amount': amount,
            'category': category,
            'date': date
        })
    
    def get_balance(self):
        # Calculate the balance by summing up all transactions
        balance = sum(transaction['amount'] for transaction in self.transactions)
        return balance
    
    def get_summary(self):
        # Summarize transactions by category
        summary = {}
        for transaction in self.transactions:
            category = transaction['category']
            if category not in summary:
                summary[category] = 0
            summary[category] += transaction['amount']
        return summary
    
    def print_summary(self):
        print("Financial Summary")
        print("-----------------")
        for category, total in self.get_summary().items():
            print(f"{category}: ${total:.2f}")
        print(f"Total Balance: ${self.get_balance():.2f}")

def main():
    manager = PersonalFinanceManager()
    
    # Example transactions
    manager.add_transaction(500, 'Income')
    manager.add_transaction(-50, 'Groceries')
    manager.add_transaction(-20, 'Entertainment')
    manager.add_transaction(200, 'Income')
    
    # Print the financial summary
    manager.print_summary()

if __name__ == "__main__":
    main()

