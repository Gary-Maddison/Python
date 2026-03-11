"""
Create an identifier pointing to a specific text message. Create a second identifier and point it to the exact same 
text message using the first identifier. Modify the second identifier by attaching a new word to the end of it. Output 
both identifiers to the screen to prove whether altering the second one affected the original first one.

"""

first = "Hello"
second = first

second = first + " World!!!"

print(first)
print(second)