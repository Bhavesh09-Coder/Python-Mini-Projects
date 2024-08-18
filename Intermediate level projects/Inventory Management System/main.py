# Project Title: Inventory Management System

# Inventory class to manage the items
class Inventory:
    def __init__(self):
        # Initialize the inventory as an empty dictionary
        self.items = {}

    def add_item(self, item_name, quantity, price):
        # Add or update an item in the inventory
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
            self.items[item_name]['price'] = price
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added/Updated {item_name}: Quantity = {self.items[item_name]['quantity']}, Price = {self.items[item_name]['price']}")

    def remove_item(self, item_name, quantity):
        # Remove an item or decrease its quantity
        if item_name in self.items:
            if self.items[item_name]['quantity'] >= quantity:
                self.items[item_name]['quantity'] -= quantity
                if self.items[item_name]['quantity'] == 0:
                    del self.items[item_name]
                print(f"Removed {quantity} of {item_name}.")
            else:
                print("Not enough quantity to remove.")
        else:
            print(f"Item {item_name} does not exist.")

    def view_items(self):
        # View all items in the inventory
        if not self.items:
            print("No items in inventory.")
        else:
            print("Inventory List:")
            for item_name, details in self.items.items():
                print(f"{item_name}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

# Function to display menu and handle user input
def menu():
    inventory = Inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Items")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            inventory.add_item(item_name, quantity, price)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(item_name, quantity)
        elif choice == '3':
            inventory.view_items()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the menu function
if __name__ == "__main__":
    menu()
