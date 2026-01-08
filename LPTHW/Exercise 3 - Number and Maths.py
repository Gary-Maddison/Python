# + plus
# - minus
# / slash
# // This is called floor division and it will round down your calculation
# * asterik
# % percent (Gives you the remainder of a division, known as Modulo)
# < less-than
# > greater-than
# <= less-than-equal
# >= greather-than-equal

# () Parentheses
# ** Exponents - Multiply a number by itself a certain number of time. 2 ** 3 = 8 (2 x 2 x 2)

# Order of Operations

# Parantheses
# Exponents
# Multiplication, Division and Modulo (As a pair, from left to right)
# Addiition and Subtraction (As a pair, from left to right)

# This is a string that will print the text between ""
print("I will now count my chickens")

# Here we do 30 / 6 = 5 + 25 = 30
print("Hens", 25 + 30 / 6)

# This line uses the modulo operator (%) to find a remainder.
# 1. (M&D group, left-to-right): First, it calculates 24 * 3 = 72.
# 2. (M&D group, left-to-right): Then, it calculates the remainder of 72 % 4, which is 0.
# 3. (A&S group): Finally, it does the subtraction: 100 - 0 = 100.

# Here we do 24 * 3 = 72 % 4 = 0 - 100 = 100
print("Roosters", 100 - 24 * 3 % 4)

# This line follows PEMDAS rules.
# 1. (M&D including % group): It first solves `4 % 2` (which is 0) and `1 / 4` (which is 0.25).
# 2. (A&S group): It then solves the rest from left to right, resulting in 6.75.

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) 

#This wll not print the result as it contained within a string
print("Is it true that 3 + 2 < 5 - 7?")

# Yes it is false as the calculation first works out 3 + 2 = 5 which is less than 5 - 7 = -2. So 5 is not less than -2
print(3 + 2 < 5 - 7)

# Here we are printing the calculation and showing the answer after he cmputer does the calculation
print("What is 3 + 2?", 3 + 2)

# Here we are printing the calculation and showing the answer after he cmputer does the calculation
print("What is 5 - 7?", 5 - 7)

# Print statement
print("Oh, thats why it's false")

# It is greater so the computer will show True
print("Is it greater?", 5 > -2)

# It is greater so the computer will show True
print("Is it greater or equal?", 5 >= -2)

# Here the computer will print False as 5 is not less than or equal to - 2
print("Is it less or equal?", 5 <= -2)