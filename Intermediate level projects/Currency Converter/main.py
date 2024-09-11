# Currency Converter

# Exchange rates relative to USD (as of the latest data)
exchange_rates = {
    'USD': 1.0,          # US Dollar
    'EUR': 0.93,         # Euro
    'GBP': 0.82,         # British Pound
    'JPY': 146.43,       # Japanese Yen
    'AUD': 1.56,         # Australian Dollar
    'CAD': 1.37,         # Canadian Dollar
    'CHF': 0.88,         # Swiss Franc
    'CNY': 7.29,         # Chinese Yuan
    'SEK': 10.63,        # Swedish Krona
    'NZD': 1.70,         # New Zealand Dollar
    'MXN': 17.50,        # Mexican Peso
    'SGD': 1.37,         # Singapore Dollar
    'HKD': 7.85,         # Hong Kong Dollar
    'KRW': 1346.37,      # South Korean Won
    'TRY': 27.16,        # Turkish Lira
    'RUB': 94.27,        # Russian Ruble
    'INR': 82.77,        # Indian Rupee
    'BRL': 4.84,         # Brazilian Real
    'ZAR': 19.26,        # South African Rand
    'MYR': 4.66,         # Malaysian Ringgit
    'AED': 3.67          # United Arab Emirates Dirham
}

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another."""
    if from_currency not in exchange_rates:
        raise ValueError(f"Currency '{from_currency}' not supported.")
    if to_currency not in exchange_rates:
        raise ValueError(f"Currency '{to_currency}' not supported.")
    
    # Convert the amount to USD, then to the target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    amount_in_target_currency = amount_in_usd * exchange_rates[to_currency]
    return amount_in_target_currency

def main():
    print("Currency Converter")
    print("Available currencies:", ', '.join(exchange_rates.keys()))
    
    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    amount = float(input("Enter the amount you want to convert: "))
    
    try:
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
