
## Unit Convertor:
"""
Unit Converter

This program allows users to convert between various units of measurement using a command-line interface.
The supported conversions are:
1. Kilometers to Miles
2. Miles to Kilometers
3. Celsius to Fahrenheit
4. Fahrenheit to Celsius
5. Kilograms to Pounds
6. Pounds to Kilograms
7. Liters to Gallons
8. Gallons to Liters

"""


# Function to convert kilometers to miles
def kilometers_to_miles(kilometers):
    # 1 kilometer is approximately 0.621371 miles
    return kilometers * 0.621371

# Function to convert miles to kilometers
def miles_to_kilometers(miles):
    # 1 mile is approximately 1.60934 kilometers
    return miles * 1.60934

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Conversion formula: (Celsius * 9/5) + 32 = Fahrenheit
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Conversion formula: (Fahrenheit - 32) * 5/9 = Celsius
    return (fahrenheit - 32) * 5/9

# Function to convert kilograms to pounds
def kilograms_to_pounds(kilograms):
    # 1 kilogram is approximately 2.20462 pounds
    return kilograms * 2.20462

# Function to convert pounds to kilograms
def pounds_to_kilograms(pounds):
    # 1 pound is approximately 0.453592 kilograms
    return pounds * 0.453592

# Function to convert liters to gallons
def liters_to_gallons(liters):
    # 1 liter is approximately 0.264172 gallons
    return liters * 0.264172

# Function to convert gallons to liters
def gallons_to_liters(gallons):
    # 1 gallon is approximately 3.78541 liters
    return gallons * 3.78541

# Main function to run the Unit Converter
def main():
    while True:
        print("\nUnit Converter")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Kilograms to Pounds")
        print("6. Pounds to Kilograms")
        print("7. Liters to Gallons")
        print("8. Gallons to Liters")
        print("9. Exit")
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            kilometers = float(input("Enter kilometers: ").strip())
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers} kilometers is {miles} miles.")
        
        elif choice == '2':
            miles = float(input("Enter miles: ").strip())
            kilometers = miles_to_kilometers(miles)
            print(f"{miles} miles is {kilometers} kilometers.")
        
        elif choice == '3':
            celsius = float(input("Enter Celsius: ").strip())
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")
        
        elif choice == '4':
            fahrenheit = float(input("Enter Fahrenheit: ").strip())
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is {celsius} Celsius.")
        
        elif choice == '5':
            kilograms = float(input("Enter kilograms: ").strip())
            pounds = kilograms_to_pounds(kilograms)
            print(f"{kilograms} kilograms is {pounds} pounds.")
        
        elif choice == '6':
            pounds = float(input("Enter pounds: ").strip())
            kilograms = pounds_to_kilograms(pounds)
            print(f"{pounds} pounds is {kilograms} kilograms.")
        
        elif choice == '7':
            liters = float(input("Enter liters: ").strip())
            gallons = liters_to_gallons(liters)
            print(f"{liters} liters is {gallons} gallons.")
        
        elif choice == '8':
            gallons = float(input("Enter gallons: ").strip())
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is {liters} liters.")
        
        elif choice == '9':
            print("Exiting the Unit Converter.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
 
