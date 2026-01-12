print("The Automated Toll Booth")

weight = float(input("Vehicle Weight KG: "))
hour = float(input("Time 24 Hour Clock: "))

if weight < 2000:
    price = 5.00 

else:
    price = 10.00

if (hour >= 7 and hour <= 9) or (hour >= 16 and hour <= 18): # Here I have entered () to keep the code tidy and easy to read.
    price = price + 2.50

if weight % 2 == 0:
    price = price - 1

total = price

print(f"Total Cost: £{price}") # Here I am using an f-string to keep everything inside the string.