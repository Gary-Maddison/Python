"""
Ask the user for a strictly three-digit whole number (e.g., 456). Without converting the number into text, mathematically 
extract the hundreds digit, the tens digit, and the ones digit. Output the sum of these three isolated digits.

"""

digital_number = int(input("Please enter a three digit number: "))

hundred = digital_number // 100
tens = (digital_number // 10) % 10
single = digital_number % 10

print(hundred + tens + single)