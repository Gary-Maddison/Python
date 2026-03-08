"""
Ask the user to type in the year they were born. Read this input from the console. Using the current year, calculate their 
approximate age. Output a sentence that seamlessly mixes text with their calculated age.

"""

current_year = 2026
year_born = int(input("What year were you born: "))
age = current_year - year_born

print(f"You are {age} years old.")