"""
Store the price of a single item, the quantity of items purchased, and a flat discount amount 
in separate containers. Calculate the final cost (price multiplied by quantity, minus the discount) 
and store it in a new container. Display a formatted receipt message showing the final calculated cost.

"""

item_price = 10.99
items_purchased = 2
discount_amount = 10
total_price = (item_price * items_purchased) - discount_amount

print(f"Total Price: {total_price}")