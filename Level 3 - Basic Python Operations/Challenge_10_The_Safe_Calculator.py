"""
Prompt the user for two separate numbers, followed by a mathematical operation choice (e.g., a choice representing addition, 
subtraction, multiplication, or division). Perform the requested calculation on the two numbers and display the answer. 
Implement a safety mechanism: if the user requests division and provides zero as the second number, prevent the calculation and 
display a friendly warning instead.

"""


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == "/" and num2 == 0:
    print("Warning: Cannot divide by zero!")
elif operation == "/":
    print("The answer is", num1 / num2)
elif operation == "+":
    print("The answer is", num1 + num2)
elif operation == "-":
    print("The answer is", num1 - num2)
elif operation == "*":
    print("The answer is", num1 * num2)
else:
    print("Error: Invalid operation.")

