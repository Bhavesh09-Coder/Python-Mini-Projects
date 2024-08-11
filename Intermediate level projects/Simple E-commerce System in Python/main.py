# Simple E-commerce System in Python

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            if product.id in self.items:
                self.items[product.id]['quantity'] += quantity
            else:
                self.items[product.id] = {'product': product, 'quantity': quantity}
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to your cart.")
        else:
            print(f"Sorry, only {product.stock} of {product.name} are available in stock.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name} (x{quantity}) - ${product.price * quantity}")
            total += product.price * quantity
        print(f"Total: ${total}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return
        self.view_cart()
        print("Checking out... Thank you for your purchase!")
        self.items.clear()

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, id, name, price, stock):
        if id not in self.products:
            self.products[id] = Product(id, name, price, stock)
            print(f"Added {name} to the store.")
        else:
            print("Product ID already exists.")

    def view_products(self):
        if not self.products:
            print("No products available in the store.")
            return
        print("Available products:")
        for product in self.products.values():
            print(f"{product.id}. {product.name} - ${product.price} (Stock: {product.stock})")

# Main execution
store = Store()
cart = ShoppingCart()

# Adding products to the store
store.add_product(1, "Laptop", 1200, 5)
store.add_product(2, "Smartphone", 800, 10)
store.add_product(3, "Headphones", 150, 20)

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        store.view_products()
    elif choice == '2':
        store.view_products()
        product_id = int(input("Enter the product ID to add to cart: "))
        quantity = int(input("Enter the quantity: "))
        if product_id in store.products:
            cart.add_to_cart(store.products[product_id], quantity)
        else:
            print("Invalid product ID.")
    elif choice == '3':
        cart.view_cart()
    elif choice == '4':
        cart.checkout()
    elif choice == '5':
        print("Exiting the store. Thank you for visiting!")
        break
    else:
        print("Invalid choice. Please try again.")
