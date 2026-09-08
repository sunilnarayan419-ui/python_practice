# number classifier
"""Given an integer, determine whether it is:
   Positive / Negative / Zero
   Even / Odd"""

class NumberClassifier:
    @staticmethod
    def classify_number(number):
        if number > 0:
            sign = "Positive"
        elif number < 0:
            sign = "Negative"
        else:
            sign = "Zero"

        if number % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"

        return sign, parity 
number_classifier = NumberClassifier()

try:
    number = int(input("Enter an integer: "))
    sign, parity = number_classifier.classify_number(number)
    print(f"The number {number} is classified as: {sign} and {parity}") 
except ValueError:
    print("Please enter a valid integer.")