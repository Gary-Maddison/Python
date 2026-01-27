password = input('Set a "Secret Password": ')
login = input("Enter Password: ")
attempts = 1

print(login)

while login != password:
    print("Access Denied")
    login = input("Enter Password: ")
    attempts += 1

print(f"Access Granted! It took you {attempts} attempts")
