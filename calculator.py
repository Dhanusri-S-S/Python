# Simple Calculator

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask for operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
