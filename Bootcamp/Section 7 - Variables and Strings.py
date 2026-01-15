tips_jar = 100  # Here we have a variable called tips_jar and inside we have put in 100
print(tips_jar) #  Here we are printing the value of what is inside the jar

tips_jar = "Nothing" # Here we are putting text inside the jar so we to use " " to show this is a string
print(tips_jar) # This now print the word Nothing

# Naming Restrictions

# Variables must start with a letter or an underscore _
# Variables are case-sensitive
# Some names are not allowed as they are used in the python language - print, input

# Data Types

# bool - True or False
# int - 1, 2, 3
# str - Unicode characters, eg. "Gary or "hghgehd"
# list - An ordered sequence of value, eg. [1, 2, 3] or ["a", "b", "c"]
# dict - A collection of key values: values, eg. {"first_name": "Gary", "last_name": "Maddison"}

# Special value called None

no_children = None # This repesents nothingness
print(type(no_children))# This is a NoneType

# Double and single quotes

print("Gary Maddison") # What you open your string with you close with
print('Gary Maddison')
print('Gary said "Hello"') # Here I want show " " within the string so I use single quotes

# String Escape Characters  

# \n - New Line

print

# \\
print("This is a backslash: \\")

# If you are double quotes within double quotes or single within single you need to use the escape character \

print("Gary said \"Hello\"")

# String Concatenation

string_one = "Hello"
string_two = "World"
print(string_one + " " + string_two) # Here we are concatenating two strings with a space in between

# You can use the += operator to add to a string variable

greeting = "Gary"
greeting += " World"    
print(greeting)  # This adds " World" to the end of the greeting variable

# Formatting Strings

x = 10
formatted = f"I've told you {x} times"  # This is a formatted string as we want to include the value of x
print(formatted)

name = "Gary" 
print(f"Hi {name}, how are you?") # Here we are using a formatted string to include the name variable

# String and Indexes

name = "lol" # Each letter is indexed [0,1,2] - Indices always start with 0
print(name[0])  # Here I am print l
print(name[1])  # Here I am printing o
print(name[2])  # Here I am print l

# Converting Data Types

decimal = 12.4445
integer = int(decimal) # Here we are converting a float into a integer, thus giving us 12


