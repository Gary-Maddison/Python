print("Mileage Convertor")

kms = float(input("Please Enter KM: "))
miles = round(kms * 0.621371, 2) # Here I am rounding the calculation to 2 decimal places
print(f"{kms}km = {miles} miles")


# String Slicing

secret_code = "PYTHON-COURSE-2026"
print(secret_code[-4])
print(secret_code[-3])
print(secret_code[-2])
print(secret_code[-1])

print(secret_code[-4:])  # This grabs everything from the 4th to last character to the end of 2026
print(secret_code[0:6])  # This grabs everything from the 0 character 0 up to N, this is the 5th character but 6 stops beforhand