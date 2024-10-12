import datetime

def budget_tracker():
    transactions = []
    
    while True:
        action = input("Choose action (add/view/summary/exit): ").lower()
        if action == 'add':
            description = input("Enter a description of the transaction: ")
            amount = float(input("Enter the amount: "))
            transaction_type = input("Is this income or expense? ").lower()
            date = datetime.date.today()
            
            transactions.append({"description": description, "amount": amount, "type": transaction_type, "date": date})
        elif action == 'view':
            for idx, trans in enumerate(transactions):
                print(f"{idx + 1}. {trans['date']} - {trans['description']} - {trans['type'].capitalize()} - ${trans['amount']:.2f}")
        elif action == 'summary':
            total_income = sum([trans["amount"] for trans in transactions if trans["type"] == 'income'])
            total_expense = sum([trans["amount"] for trans in transactions if trans["type"] == 'expense'])
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net: ${total_income - total_expense:.2f}")
        elif action == 'exit':
            break

budget_tracker()
