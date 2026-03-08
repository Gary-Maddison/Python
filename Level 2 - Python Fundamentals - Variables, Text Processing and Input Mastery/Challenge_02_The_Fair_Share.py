"""
Imagine you have 237 gold coins and a party of 5 adventurers. Calculate how many whole coins 
each adventurer receives, and calculate how many coins are left over for the guild master. 
Output both results clearly.

"""

gold_coins = 237
people = 5
coins_per_person = gold_coins // people
coins_remaining = gold_coins % people 

print(f"Each person receives {coins_per_person} and {coins_remaining} coins will remian.")