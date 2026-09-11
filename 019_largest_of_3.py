# LARGEST OF THREE NUMBERS 

def largest_of_three(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    return largest

# Example usage
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest_number = largest_of_three(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}") 