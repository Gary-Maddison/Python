"""
Ask the user to provide an X coordinate and a Y coordinate on a 2D plane. Determine and display exactly which of the four 
mathematical quadrants the point resides in. Additionally, identify and handle the special cases where the point lies exactly on 
the X-axis, exactly on the Y-axis, or directly at the center origin (0,0).

"""

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

# Checking special cases first
if x == 0 and y == 0:
    print("Directly at the center origin (0,0)")
elif x == 0:
    print("Exactly on the Y-axis")
elif y == 0:
    print("Exactly on the X-axis")

# Checking the 4 quadrants
elif x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
else:
    print("Fourth quadrant")