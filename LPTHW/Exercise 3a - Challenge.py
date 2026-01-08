# The Scenario: You are preparing for your first term at Arden.
# You have a starting budget of £200.00.
# You buy 3 Python textbooks for £32.50 each.
# You buy 2 notebooks for £4.25 each.
# The Goal: Write a script that:

# Calculates the Total Spent.
# Calculates the Remaining Balance.
# Uses a comparison operator (like > or <) to print a True/False statement answering: 

# "Is my remaining balance enough to buy a £75.00 software license?

money = 200 # This shows how much money I have
total_spent = (32.50 * 3) + (4.25 * 2) # Here I am calculating what I spent
money_left = money - total_spent

print("I have spent £", total_spent) # This shows what I have spent

print("Is my remaining balance enough to buy a £75.00 software license?", money_left > 75, "I have £", money_left, "left to spend") # This uses a True or False statement to show if I havce enough money to purchase another item