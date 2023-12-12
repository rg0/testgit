#write a program to add 2 numbers
def add_numbers(num1, num2):
    return num1 + num2

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
except ValueError:
    print("Error: Please enter a valid number.")