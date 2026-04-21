"""
Start with a value of 20. Decrease the value by 1 repeatedly, outputting the current value each time. 
The process must stop completely once the value drops below 0. Afterward, output a final completion message.

"""
value = 20 

while value > 0:
    value -= 1
    print(value)