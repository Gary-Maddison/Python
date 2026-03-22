"""
Create a multi-step calculation. First, find the leftover value when a specific order number is divided by 5. Next, 
take that leftover value and raise it to the power of 3. Add this result to a running total using a shorthand updating technique. 
Finally, display the final total underneath a long-form, multi-line receipt header.

"""
total = 0
order_number = 49
left_over = order_number % 5

left_over = left_over ** 3

total += left_over

print("""
-------------------   
Your Total Order
      
Have a nice day.      
-------------------    
""")

print("Total", total)