def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# User Input and Function Call
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")