# for loops

for char in "hello":  # The word char is a temp varaible storing what comes after the word in, for and in stay the same
    print(char)

for x in range(1, 10):  # X is the temp variable and range is what we are printing 1 - 9
    print(x)

# Ranges

# range(7) gives you integers 0 through 6
# range (1,8) will give you integers from 1 to 7
# range (1, 10, 2) The thrid number is the step, meaning how many to skip
# range(7, 0, -1) Here we are using a step but are going backwards 1 at a time

for num in range(10):
    print(num)
for num in range(0, 20, 2):
    print(num)

# this will work out 10, 21 odd numbers and add them togethor

x = 0
for num in range(10, 21):
    if num % 2 != 0:
        x += num
print(x)

# This will print a line of text a given number of times

times = int(input("How many times do I have to tell you? "))
for lines in range(times):
    print("Clean up Your Room")

# While Loops continue to execute whilst something is True

user_response = None  # This will loop until they input please
while user_response != "please":
    user_response = input("You did not say the word please: ")

msg = input("What is the secret password?")
while msg != "secret":
    print("WRONG!")
    msg = input("What is the secret password? ")
print("Correct")  # This only runs when the while loop finishes

# Convert a For loop into a While loop

for num in range(1, 11):
    print(num)

num = 1
while num < 11:  # This will run until it reaches 10
    print(num)
    num += 1

# Break - Exit a Loop in a controlled manner

while True:
    command = input("type 'exit' to exit: ")
    if (command == "exit"):
        break

for x in range(1, 101):
    print(x)
    if x == 3:
        break


times = int(input("Hoew many times do I have to tell you?"))
for time in range(times):
    print("Clean up your room!")
    if time >= 3:
        print("Are you listening to me? ")
        break
