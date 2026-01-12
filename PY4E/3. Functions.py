
def computepay(hours, rate):
    if hours <= 40 :
        pay = hours * rate 

    else:
        ot = hours - 40
        pay = 40 * rate + (ot * rate * 1.5)

    return(pay)

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

p = computepay (hours, rate) # Here I am calling up the variables hours and rate and placing this in a variable
print(f"Your Total Pay: £ {p}") # Here I am printing the variable p