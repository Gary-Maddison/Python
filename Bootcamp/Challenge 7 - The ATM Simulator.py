cust_pin = 1234
starting_balance = 100
audit_count = 0
pin_attempts = 3
pin = 0

# This is the pin checker in order to enter the main program
while pin != cust_pin:
    pin = int(input("Please enter your pin: "))
    if pin == cust_pin:
        break
    else:
        pin_attempts -= 1
        if pin_attempts == 0:
            print("Incorrect Pin. Please try again later!")
            exit()
        else:
            print(f"Incorrect Pin - {pin_attempts} remaining ")

while True:

    print("""
    \t1. Check Balance:
    \t2. Deposit Money
    \t3. Withdraw Money
    \t4. Exit    
    """)

    user_choice = int(input("Please Select: "))

    if user_choice == 1:
        print(f"Your Balance: £{starting_balance}")
    elif user_choice == 2:
        deposit_amount = float(input("Deposit Amount: "))
        print(f"£{deposit_amount} as been credited into your account")
        starting_balance += deposit_amount
        audit_count += 1
    elif user_choice == 3:
        withdrawal_amount = float(input("Withdrawal Amount: "))
        if withdrawal_amount > starting_balance:
            print("Insufficient Funds")
        else:
            starting_balance -= withdrawal_amount
            print(f"£{withdrawal_amount} as been withdrawn from your account")
            audit_count += 1
    else:
        break

print(
    f"You Balance Today £{starting_balance}. Total Transactions Completed {audit_count}")
