"""
You have a sequence of item weights. Traverse this sequence by determining its total size and using 
a counter that increases step-by-step. Output each weight using this counter. 

"""

weights = [45, 87, 22, 34, 88, 99]
count = len(weights)
index = 0

while index < count:
    print(weights[index])
    index += 1