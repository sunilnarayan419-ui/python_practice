# temperatur_classifier 
"""Temperature Classifier Given a temperature, classify it as: < 0 → Freezing 0–15 → Cold 16–30 → Moderate 31–40 → Hot

40 → Extreme Heat"""

class TemperatureClassifier:

    @staticmethod
    def classify_temperature(temperature):
        if temperature < 0:
            return "Freezing"
        elif 0 <= temperature <= 15:
            return "Cold"
        elif 16 <= temperature <= 30:
            return "Moderate"
        elif 31 <= temperature <= 40:
            return "Hot"
        else:
            return "Extreme Heat"

temperature_classifier = TemperatureClassifier() 

try:
    temperature = float(input("Enter the temperature: "))
    classification = temperature_classifier.classify_temperature(temperature)
    print(f"The temperature {temperature}°C is classified as: {classification}")
except ValueError:
    print("Please enter a valid number for the temperature.") 