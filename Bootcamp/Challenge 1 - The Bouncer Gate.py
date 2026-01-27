# This converts the string into an integer
age = int(input("How old are you? "))

# This lowers the input to lowercase. Make sure when its called the string is also lower case.
member = input("Do you have a membership card? (Yes/No) ").lower()

if age >= 18 and member == "yes":
    print("Welcome to the club!")
elif age < 18:
    print("Sorry, you are too young")
else:
    print("You need a membership")
