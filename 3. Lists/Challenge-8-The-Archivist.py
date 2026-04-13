"""
You have an existing collection of scrambled historical periods. Reorganize them in exact 
reverse alphabetical order. However, you must do this in a way that generates a brand new organized 
collection, leaving the original scrambled collection completely untouched.

"""

years = [1944, 2017, 1988, 2026, 2022, 2021]

sorted_list = sorted(years)
sorted_list.sort(reverse=True)

print(years)
print(sorted_list)