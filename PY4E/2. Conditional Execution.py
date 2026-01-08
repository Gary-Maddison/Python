hrs = input("Enter Hours: ")  # 45
h = float(hrs)

rate = input("Enter Hourly Rate: ") # 10.5
r = float(rate)

if h > 40 :
    ot = h - 40
    print("Your Wage this week is:", 40 * r + (ot * r * 1.5))

else:
    print("Your Wage this week is: £", h * r)

