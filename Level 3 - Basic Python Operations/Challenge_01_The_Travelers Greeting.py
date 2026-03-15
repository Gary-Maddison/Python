"""
Ask the user for their name and their current age. Calculate the year they were born (assuming the current year is 2026). 
Display a single welcome message that greets them by name and reveals their calculated birth year.

"""

name = input("Enter your name: ") 
age = int(input("How old are you: "))
year = 2026

print(f"Hi {name} you were born in {year - age}")


