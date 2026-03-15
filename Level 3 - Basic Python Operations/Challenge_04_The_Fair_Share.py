"""
Ask the user for a total restaurant bill amount and the number of people splitting the bill. Calculate how much each person owes. 
Display a message stating the exact amount each person must pay.

"""

total_bill = float(input("Total bill £"))
people = int(input("Total people: "))
split = total_bill / people

print(f"Each person owes £{split}")