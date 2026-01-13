
def get_guess ():

    guess = ""

    while True:
    
        try:
            guess = int(input("Enter a number? "))
        
            if guess < secret_number:
                print("Guess is too low")

            elif guess > secret_number:
                print("Guess is too high")

            else:
                print("You Win")
                break

        except:
            print("Please enter a number")
        
    return(guess)

secret_number = 42

while get_guess() != secret_number:
    print()





    








    


