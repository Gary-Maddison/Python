print("The Bill Splitter")

total_bill = float(input("How much is the bill?: ")) # We are putting a float to convert it from a string
people = float(input("How many people?: "))
tip = float(input("How big is the tip?: ")) 

tip_amount = (total_bill * (tip / 100))

print("Your total Bill including tip is: £", total_bill + tip_amount, sep="")
print("Each person owes: £", (total_bill + tip_amount) / people, sep="") # This is placed in brackets as we need the additional doing first due to PEMDAS.

