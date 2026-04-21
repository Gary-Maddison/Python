"""
You have a sequence of colors. Inspect each color one by one. If you encounter the color "crimson", output "Match found!" 
and immediately halt the entire inspection process so no subsequent colors are checked. 

"""

colours = ["Blue", "Black", "Red", "Orange", "Crimson", "Purple"]

for colour in colours:
    print(colour)
    if colour == "Crimson":
        print("Match Found!")
        break


