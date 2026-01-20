import random

print("--- Welcome to the Guessing Game ---")

while True:
    # 1. Reset the game state for a new round
    random_number = random.randint(1, 10)
    guess = None  # Start with None so the inner loop definitely runs

    # 2. The Guessing Loop
    while guess != random_number:
        guess = int(input("Choose a number between 1 and 10: "))

        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print("Too High")

    # 3. The Win Sequence
    print(f"You Win! The number was {random_number}")

    # 4. The Replay Logic
    play_again = input("Play Again? (Y/N): ").upper()  # Normalize to uppercase
    if play_again == "N":
        break

print("Thanks for Playing!")
