"""
Ask the user for the total price of an item and the amount of money they are handing to the cashier. If they provide less money than the price, 
tell them exactly how much more they owe. If they provide the exact amount, thank them. If they provide too much, calculate and 
display their exact change.

"""
item_price = float(input("Item price £"))
cash = float(input("Cash £"))

cashier = item_price - cash

if item_price > cash:
    print(f"You still owe £{cashier}")

elif item_price < cash:
    print(f"You have £ {(cashier + cashier) - cashier} change")

else:
    print("Thank you for your payment")