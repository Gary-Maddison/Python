cars = 100  # Here we have a variable called cars with 100 stored inside 
space_in_car = 4.0 # This is a floating point number but you couod just use 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # Here we are subtracting an amount stored in variable 
cars_driven = drivers # Here we are using the variable drivers and creating a seperate variable
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")

# Here I doing a line break to shorten the length of code

print("We need to put about", average_passengers_per_car, 
      "in each car")
