"""
Ask the user for their age. If they are 21 or older, welcome them to the VIP section. If they are exactly 18, 19, or 20, 
welcome them to the venue but restrict them from the VIP section. If they are under 18, deny them entry entirely.

"""

age = int(input("Enter age: "))

if age >= 21:
    print("Welcome to the VIP section")

elif age >= 18:
    print("Welcoem to the venue - VIP restricted")

else:
    print("Entry Denied!!!")