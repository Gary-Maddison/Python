import random

print("--- Welcome to the Professional RPS Arena ---")

while True:
    # 1. Let the user decide the match length
    target_score = int(input("Best of how many games? (e.g., 3 or 5): "))
    # Logic for "Best of": 2 wins for Bo3, 3 for Bo5
    wins_needed = (target_score // 2) + 1

    p1_score = 0
    p2_score = 0

    # 2. Match Loop: Keep playing until someone hits the win target
    while p1_score < wins_needed and p2_score < wins_needed:
        print(f"\nScore: Player 1: {p1_score} | Computer: {p2_score}")

        player_1 = input("Player 1: rock, paper, or scissors: ").lower()

        if player_1 not in ["rock", "paper", "scissors"]:
            print("Invalid input, try again!")
            continue  # Skips the rest of the loop and asks again

        player_2 = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {player_2}")

        # Your core logic updated with score counters
        if player_1 == player_2:
            print("It's a Tie!")
        elif (player_1 == "rock" and player_2 == "scissors") or \
             (player_1 == "paper" and player_2 == "rock") or \
             (player_1 == "scissors" and player_2 == "paper"):
            print("Player 1 wins this round!")
            p1_score += 1
        else:
            print("Computer wins this round!")
            p2_score += 1

    # 3. Final Match Results
    if p1_score > p2_score:
        print(f"\nCONGRATULATIONS! You won the Best of {target_score}!")
    else:
        print(f"\nGAME OVER! The computer won the Best of {target_score}.")

    # 4. Play Again Gate
    again = input("\nDo you want to play a whole new match? (y/n): ").lower()
    if again != "y":
        break

print("Thanks for playing!")
