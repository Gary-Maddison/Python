"""
Create two text-based variables, both holding negative numerical values wrapped in quotes. Transform these text values 
into actual mathematical values. Add them together to find the total, transform that final total back into a text 
format, and merge it with a congratulatory message to display on the screen.

"""

number_one = "-1977"
number_two = "-1966"

total = int(number_one) + int(number_two)

string_number = str(total)

print(f"Here I have converted the sum of two integers into a string {string_number}")