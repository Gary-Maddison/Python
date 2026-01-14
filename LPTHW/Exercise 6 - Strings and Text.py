types_of_people = 10 # A variable with a value of 10
x =f"There are {types_of_people} types of people" # Using an f-string to keep everythying including pulling up the variable within the string. 

binary = "binary" # A variable with a value called binary
do_not = "don't" # A variable with a value called don't
y = f"Those who know {binary} and those who {do_not}" # Here we are using an f-string and pulling 2 variables into it.

print(x)
print(y)

print(f"I said {x}")
print(f"I also said: '{y}'")

hilarious = False # Here we are setting a variable to false
joke_evaluation = "Isn't that joke so funny?! {}" # Here we are creating a variablke with an empty string

print(joke_evaluation.format(hilarious)) # Here we are print the named variable however the .format() allows us to insert the variable hilarous into the print fuction.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # Here we are combing varaibles to craete one string. This is called concatenation
