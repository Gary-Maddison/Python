"""
You have a sequence of base prices. Generate a brand-new sequence where every price has been multiplied by 1.5. 
You must accomplish this entire generation process using a single, elegant line of logic.

"""

base_prices = [1.99, 3.98, 3.45, 2.99, 6.77, 1.99]

multiplied_one_and_half = [num * 1.5 for num in base_prices]

print(multiplied_one_and_half)