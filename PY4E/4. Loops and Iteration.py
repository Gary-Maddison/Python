# --- SCRIPT 1: A "Countdown" Loop (Definite Iteration) ---

n = 10  # Initialize an iteration variable; this is a 'named place in memory' to track our count.

while n > 0:   # A conditional statement: the loop runs as long as the 'box' labeled 'n' is greater than 0
    print(n)   # Display the current value of n to the user
    n = n - 1  # Reassignment: update 'n' by subtracting 1. This prevents an infinite loop

print('Blastoff!') # The loop has finished (n is 0), so the program moves to the next sequential line


# --- SCRIPT 2: An "Exit on Command" Loop ---

while True:    # Creates an infinite loop because 'True' is a constant that never changes
    line = input('Test') # Pauses the program to read data from the user
    if line == 'done':   # Check if the user typed the exact reserved exit word 'done'
        break            # The "Emergency Exit": jumps out of the loop immediately
    print(line)          # If the user didn't type 'done', print whatever they entered.

print('Done')


# --- SCRIPT 3: A "Smart" Loop with Filtering ---

while True: # 1. Create an 'Infinite Loop' that runs until we say 'break'
    
    user_data = input('Type something (or "done" to quit): ') # 2. Ask user for data 

    # 3. Handle Empty Input (Safety Check)
    if len(user_data) == 0:
        continue # Skip to the top if the user just pressed Enter

    # 4. Filter out Comments
    if user_data[0] == '#': 
        print("Skipping comment...") # Added for clarity
        continue # Jump back to the top of the loop

    # 5. Check for Exit Command
    if user_data == 'done':
        break # "Emergency Exit": Stop the loop entirely 

    # 6. Process the Data
    print("You entered:", user_data) # Only runs if steps 4 and 5 were bypassed

# 7. Final Output
print('--- Script Closed ---')


# A Simple Definate Loop

for i in [5, 4, 3, 2,1]: # This will loop through the list
    print (i)
print('Blastoff')


# Finding the largest value

largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far)
print('After', largest_so_far)
