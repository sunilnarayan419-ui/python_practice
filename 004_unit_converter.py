# unit converter 

class UnitConverter:

    @staticmethod
    def meters_to_kilometers(meters):
        return meters / 1000

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * 1000

unit_converter = UnitConverter()

try:
    distance = float(input("Enter the distance: "))
    unit = input("Enter the unit (M for meters, KM for kilometers): ").strip().upper()

    if unit == "M":
        result = unit_converter.meters_to_kilometers(distance)
        print(f"{distance} meters is equal to {result:.2f} kilometers")

    elif unit == "KM":
        result = unit_converter.kilometers_to_meters(distance)
        print(f"{distance} kilometers is equal to {result:.2f} meters")

    else:
        print("Invalid unit. Please enter 'M' for meters or 'KM' for kilometers.")
except ValueError:
    print("Invalid distance. Please enter a number.")