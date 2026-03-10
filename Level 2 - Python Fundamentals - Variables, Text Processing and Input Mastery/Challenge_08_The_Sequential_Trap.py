"""
Write a program that asks the user for a highly precise decimal number (like their exact bank balance down to the cent). 
Read it. Immediately after, ask them for their full name and read it. Output the name and the balance. 

(Note: Watch carefully how the program behaves when you test this—you must ensure both pieces of information are 
successfully captured!)

"""

balance = float(input("Please enter your bank balance £"))
name = input("Please enter your full name: ").strip().upper()

print(f"{name} your balance is £{balance}")

