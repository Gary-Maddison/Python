"""
Ask the user to provide a number. Determine mathematically whether the given number is even or odd, and 
display a message explicitly stating the result.

"""

number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even Numbrer")

else:
    print("Odd number")