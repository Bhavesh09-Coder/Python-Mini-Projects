## 3. Temperature Conversion Tool¶
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(c: float) -> float:
    return c + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(k: float) -> float:
    return k - 273.15

# Example usage of temperature conversion functions
c = 25.0
f = celsius_to_fahrenheit(c)
k = celsius_to_kelvin(c)
print(f"{c}°C is {f}°F and {k}K")

f = 77.0
c = fahrenheit_to_celsius(f)
print(f"{f}°F is {c}°C")

k = 300.0
c = kelvin_to_celsius(k)
print(f"{k}K is {c}°C")
def add(*args):
    y = 1
    for i in args:
        y = y*i
    return y
v = add(1,2,3,4,3,4) 
print(v)
288
 
