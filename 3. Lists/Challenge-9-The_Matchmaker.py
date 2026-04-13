"""
You are given two separate collections: one containing a set of first names, and another 
containing a set of corresponding ages. Combine these two sets so that each name is directly 
grouped with its matching age. The final result must be a viewable, unified collection of paired items.

"""

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)
converted_names_and_heights = list(names_and_heights)

print(converted_names_and_heights)