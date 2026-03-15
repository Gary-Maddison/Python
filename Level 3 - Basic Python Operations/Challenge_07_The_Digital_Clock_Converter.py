"""
Ask the user for a very large amount of seconds (e.g., 5000). Convert this total into a traditional time format: calculate the 
total full hours, the remaining full minutes, and the leftover seconds. Display the final broken-down duration.

"""

seconds = int(input("Enter seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60

print(f"The time is {hours} hours, {minutes} minutes, and {sec} seconds.")