"""
Ask the user to provide the length and width of a room. Calculate both the total floor area (for new carpet) and the perimeter (for new baseboards). 
Display both final measurements clearly on the screen.

"""

width = int(input("Please enter width: "))
length = int(input("Please enter length: "))
floor = width * length
perimeter = (width * 2) + (length * 2) 

print(f"The floor are is {floor} and the perimeter is {perimeter}")