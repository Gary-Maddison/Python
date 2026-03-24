"""
Construct a space weight calculator. Given an individual's Earth weight and a numerical selection representing a 
destination, calculate and output the adjusted weight for that specific destination. Support exactly six 
distinct destinations, ensuring each uses its own unique mathematical conversion rate before outputting the final result.

"""

weight = 185
planet = 3

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)