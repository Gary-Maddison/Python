"""
Create a collection of five different names. Replace the third name with a completely new name. 
Then, retrieve and display the very last name in the collection using backward positional tracking.

"""

names = ["Gary", "Leasa", "Ben", "Liam", "Jack"]

names[2] = "Kathryn"

print(names[-1])