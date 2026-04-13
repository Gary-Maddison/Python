"""
Start with a collection containing several duplicate items. Calculate and output exactly 
how many total items exist in the collection. Then, calculate and output exactly how many times 
one specific duplicate item appears.

"""

cars = ["BMW", "Ford", "Jaguar", "Ford", "Nissan", "BMW"]

print(len(cars))

BMW = cars.count("BMW")
print(BMW)