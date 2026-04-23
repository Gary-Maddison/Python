"""
You have a sequence of numbers (both positive and negative). Generate a brand-new sequence based on this rule: if the number is negative, 
multiply it by 2; otherwise, multiply it by 3. You must accomplish this entire transformation and evaluation process using a single, elegant line of logic.

"""

numbers = [23, -4, 66, -34, 89, 22, -12, 66, -89, 22]

new_number = [num * 2 if num < 0 else num * 3 for num in numbers]

print(new_number)