age = int(input("How old are you? "))
weekend = input("Is it a weekend (Yes/No) ").lower()
price = 0

if age < 12:
    price += 5
elif age >= 65:
    price += 7
elif weekend == "yes":
    price += 12
else:
    price += 10

print(f"Your ticket price is £{price}")
