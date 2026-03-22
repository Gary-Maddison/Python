"""
Set up a starting shopping cart balance of zero. Step-by-step, accumulate the cost of three different clothing items into 
that balance using a shorthand updating technique. Display the final accumulated balance.

"""

cart_balance = 0
jumper = float(10.99)
shoes = float(49.99)
pants = float(39.99)

cart_balance += jumper
cart_balance += shoes
cart_balance += pants

print(cart_balance)