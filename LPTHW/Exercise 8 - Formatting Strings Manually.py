
# Create a variable named 'formatter' that acts as a template with 4 'holes' or slots
formatter = "{} {} {} {}"

# Take the template and plug in 4 integers (1, 2, 3, 4)
print(formatter.format(1, 2, 3, 4))

# Take the template and plug in 4 strings ('one' through 'four')
print(formatter.format("one", "two", "three", "four"))

# Take the template and plug in 4 Boolean values (True/False)
print(formatter.format(True, False, True, False))

# Pass the 'formatter' string into itself four times, resulting in a string of 16 curly braces
print(formatter.format(formatter, formatter, formatter, formatter))

# Take the template and plug in 4 longer strings.
# We use line breaks and commas to make it easier for humans to read.
print(formatter.format(
    "Try your",
    "Own text here.",
    "Maybe a poem",
    "Or a song about fear"
))
