def currency_converter():
    rates = {'USD_to_EUR': 0.85, 'EUR_to_USD': 1.18, 'USD_to_INR': 74.15, 'INR_to_USD': 0.013}
    
    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD/EUR/INR): ").upper()
    to_currency = input("Convert to (USD/EUR/INR): ").upper()
    
    conversion_key = f"{from_currency}_to_{to_currency}"
    
    if conversion_key in rates:
        converted_amount = amount * rates[conversion_key]
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion rate not available.")

currency_converter()
