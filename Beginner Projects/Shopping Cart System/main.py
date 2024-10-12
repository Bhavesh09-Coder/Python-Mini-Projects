def shopping_cart():
    cart = []
    prices = {'apple': 1.0, 'banana': 0.5, 'orange': 0.8, 'grape': 2.0}
    
    while True:
        action = input("Add/Remove/View/Checkout: ").lower()
        if action == 'add':
            item = input("Enter item to add: ").lower()
            if item in prices:
                cart.append(item)
                print(f"{item} added to the cart.")
            else:
                print(f"{item} is not available.")
        elif action == 'remove':
            item = input("Enter item to remove: ").lower()
            if item in cart:
                cart.remove(item)
                print(f"{item} removed from the cart.")
            else:
                print(f"{item} is not in the cart.")
        elif action == 'view':
            print(f"Cart: {', '.join(cart)}")
        elif action == 'checkout':
            total = sum(prices[item] for item in cart)
            if total > 10:
                total *= 0.9  # Apply 10% discount for total > 10
            print(f"Total amount: ${total:.2f}")
            break

shopping_cart()
