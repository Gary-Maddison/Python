"""
Take two distinct, pre-existing collections of numbers and merge them into a single unified sequence. 
From this combined sequence, extract a smaller segment containing only the first three numbers.

"""

number_1 = [2, 3, 4, 4]
number_2 = [4, 5, 6, 7, 8]

number_3 = number_1 + number_2

print(number_3)

sliced_numbers = number_3[0:3]

print(sliced_numbers)