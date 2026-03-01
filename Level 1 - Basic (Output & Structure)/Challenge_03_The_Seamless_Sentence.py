"""
Display a complete sentence composed of four separate words. You must use four distinct output instructions, 
but the final result must appear on the screen as a single, continuous line with appropriate spacing."""

print("The ", end = '' )
print("year ", end = '' )
print("is ", end = '' )
print(2026)

# The "Pythonic" way to do what you wrote:
print("The", "year", "is", 2026, sep=" ") 

# Or if you wanted no spaces at all:
print("The", "year", "is", 2026, sep="")