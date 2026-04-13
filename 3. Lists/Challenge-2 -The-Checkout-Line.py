"""
Start with a collection of three grocery items. Place a fourth item at the very end. 
Then, eliminate a specific item from the collection by referencing its exact name, rather than its position.

"""

groceries = ["apples", "oranges", "pears"]

groceries.append("grapes")

groceries.remove("oranges")

print(groceries)