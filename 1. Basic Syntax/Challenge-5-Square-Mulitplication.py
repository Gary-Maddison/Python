"""
Determine the total number of fabric squares needed to create a specific number of square-shaped quilts. You must 
calculate the area of one quilt by raising a side length to a power, and then multiply that by the number of people 
requesting a quilt. Display the final number.

"""

people = 5
side = 10 

print(people * (side ** 2))