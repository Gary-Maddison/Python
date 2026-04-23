"""
You have a sequence of user ages. Inspect each age. If the age is strictly less than 18, immediately 
skip to the next age without doing anything. Otherwise, output the age.

"""

user_ages = [34, 17, 16, 66, 23, 11, 35, 77 ,34 ,54 ,11]

for age in user_ages:
    if age < 18:
        continue
    print(age)