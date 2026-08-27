# simple calculator program 

import math


class Calculator:
    """This is a simple calculator to demonstrate the use of OOPS"""

    def __init__(self): 
        self.result = 0 
        self.history = [] 

    def add(self, a, b):
        """This method adds two numbers"""
        self.result = a + b 
        self.history.append(f"Added {a} to {b} got {self.result}")
        return self.result

    def subtract(self, a, b):
        """This method subtracts two numbers"""
        self.result = a - b 
        self.history.append(f"Subtracted {b} from {a} got {self.result}")
        return self.result

    def multiply(self, a, b):
        """This method multiplies two numbers"""
        self.result = a * b 
        self.history.append(f"Multiplied {a} with {b} got {self.result}")
        return self.result

    def divide(self, a, b):
        """This method divides two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b 
        self.history.append(f"Divided {a} by {b} got {self.result}")
        return self.result

    def power(self, a, b):
        """This method raises a number to the power of another"""
        self.result = a ** b 
        self.history.append(f"Raised {a} to the power of {b} got {self.result}")
        return self.result 

    def sqrt(self, a):
        """This method calculates the square root of a number"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        self.result = math.sqrt(a) 
        self.history.append(f"Calculated square root of {a} got {self.result}")
        return self.result 

    def log(self, a, base=math.e):
        """This method calculates the logarithm of a number with a given base"""
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        self.result = math.log(a, base) 
        self.history.append(f"Calculated log of {a} with base {base} got {self.result}")
        return self.result 

    def exp(self, a):
        """This method calculates the exponential of a number"""
        self.result = math.exp(a) 
        self.history.append(f"Calculated exponential of {a} got {self.result}")
        return self.result 

def main(): 

    calc = Calculator() 
    operations = {
        '1': ('Add', calc.add), 
        '2': ('Subtract', calc.subtract), 
        '3': ('Multiply', calc.multiply), 
        '4': ('Divide', calc.divide), 
        '5': ('Power', calc.power), 
        '6': ('Square Root', calc.sqrt), 
        '7': ('Logarithm', calc.log), 
        '8': ('Exponential', calc.exp) 
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("9. View History")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == '9':
            print("\nCalculation History:")
            for entry in calc.history:
                print(entry)
            continue
        elif choice in operations:
            operation_name, operation_func = operations[choice]
            try:
                if choice in ['6', '7', '8']:  # Single operand operations
                    a = float(input(f"Enter number for {operation_name}: "))
                    result = operation_func(a)
                else:  # Two operand operations
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    result = operation_func(a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please try again.")
    