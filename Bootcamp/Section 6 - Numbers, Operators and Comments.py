print(34) # This is a integer
print(type(34)) # Here the function type tells us what class we have

print(2.33) # This is a float 
print(type(2.33)) # This tells us we have a float class

print(10 + 22.33) # If you add an integer and a float python will give you a float
print(type(10 + 22.33)) # This is telling us we haver a float class

# Common Operators

# Addition +
# Subtraction -
# Multiplication *
# Division /
# Exponentional **
# Modulo %
# Integer Division //

print(10/2) # A division always returns back a float, even when dividing ints
print(2 ** 3) # This is 2 to the 3 power giving us 8
print(10 % 3) # Here we are using modulo so it gives us the remiander giving us 1
print(10 // 3) # This operation will round down the division giving us 3 instead of 3.333

# Order of Operations

# P - Parenthesis ()
# E - Exponents ** (So 2 to power of 3 = 2 * 2 * 2 = 8)
# M - Multiplication *
# D - Division /
# A - Addition +
# S - Subtraction -


total_pence = 592
coins = total_pence // 200  # Here we are working out how many £2 coins fit inside 592p
print(coins)

change = total_pence % 200  # Here we are working out how much change we will have left over
print(change)

print(-10 % 3) # This return a postive number back and not a negative