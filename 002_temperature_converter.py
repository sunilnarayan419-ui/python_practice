# Temperature Converter 

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9


temperature_converter = TemperatureConverter()

try:
    temperature = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit == "C":
        result = temperature_converter.celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")

    elif unit == "F":
        result = temperature_converter.fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")

    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    print("Invalid temperature. Please enter a number.")