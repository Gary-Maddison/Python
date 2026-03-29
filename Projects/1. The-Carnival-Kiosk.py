"""
- **Payment Processing:** If the user is eligible, check if they have enough money in their wallet 
to afford their specific ticket price. If they do, deduct the price from their wallet balance and grant 
them access. If they do not, deny them access due to insufficient funds.

"""

# 1. Initial Setup
user_name = "Gary"
age = 47
height = 87
wallet_balance = 159
daily_visitors = 124
ticket_cost = 0

# Boolean Tracking Variables
discount = False
has_funds = True

# Welcome Message
print("""
Welcome """ + user_name + """ to "Codey's Cool Carnival"
""")

# 2. Silent Calculations
lucky_visitor = daily_visitors % 7
ride_eligibility = age >= 13 and height >= 54

# Ticket Purchasing Logic
if ride_eligibility and lucky_visitor == 0:
    ticket_cost = 10.00
    if wallet_balance >= ticket_cost:
        wallet_balance -= ticket_cost
        discount = True
    else:
        has_funds = False
        
elif ride_eligibility and lucky_visitor != 0:
    ticket_cost = 25.00
    if wallet_balance >= ticket_cost:
        wallet_balance -= ticket_cost
    else:
        has_funds = False

# 3. Final Output (Control Flow & Concatenation)
if discount and ride_eligibility and has_funds:
    print("Congratulations " + user_name + "! You got the lucky discount and bought a ticket. You have $" + str(wallet_balance) + " left.")
elif ride_eligibility and has_funds:
    print("Enjoy the ride " + user_name + "! You have $" + str(wallet_balance) + " left.")
elif ride_eligibility and not has_funds:
    print("You do not have sufficient funds to ride.")
else:
    print("Sorry " + user_name + " you are not tall enough to ride. You have " + str(wallet_balance) + " left.")