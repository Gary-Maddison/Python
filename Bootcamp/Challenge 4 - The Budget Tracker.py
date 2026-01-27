budget = float(input("What is your daily budget? "))
total_spent = 0

while total_spent < budget:
    spend = float(input("How much did you spend? "))
    total_spent += spend
    remaining = budget - total_spent
    if remaining < 0:  # I am using an if statment here so the user does not get a -£ figure remaining
        break  # This pulls the user out of the while loop
    else:
        print(f"You have £{remaining} remianing")

print(f"Budget Depleted! You spent a total of £{total_spent}")
