"""
Establish a starting balance of 1500. Using only the variable itself and shorthand operators (do not write the variable name twice in a single calculation), 
simulate a deposit of 400, followed by a withdrawal of 250. Finally, increase the balance by exactly one unit using the shortest 
possible syntax. Output the final balance.

"""

starting_balance = 1500

starting_balance += 400
starting_balance -= 250
starting_balance += 1

print(starting_balance)