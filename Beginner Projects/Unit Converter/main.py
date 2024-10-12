def convert_units():
    conversions = {
        'length': {'km_to_miles': 0.621371, 'miles_to_km': 1.60934},
        'weight': {'kg_to_pounds': 2.20462, 'pounds_to_kg': 0.453592},
        'temperature': {'c_to_f': lambda c: (c * 9/5) + 32, 'f_to_c': lambda f: (f - 32) * 5/9}
    }
    
    unit_type = input("Choose unit type (length/weight/temperature): ").lower()
    
    if unit_type == 'length':
        km = float(input("Enter the value in kilometers: "))
        print(f"{km} km = {km * conversions['length']['km_to_miles']:.2f} miles")
        
    elif unit_type == 'weight':
        kg = float(input("Enter the value in kilograms: "))
        print(f"{kg} kg = {kg * conversions['weight']['kg_to_pounds']:.2f} pounds")
        
    elif unit_type == 'temperature':
        temp_type = input("Convert from (C/F): ").lower()
        temp = float(input("Enter the temperature: "))
        if temp_type == 'c':
            print(f"{temp}°C = {conversions['temperature']['c_to_f'](temp):.2f}°F")
        else:
            print(f"{temp}°F = {conversions['temperature']['f_to_c'](temp):.2f}°C")

convert_units()
