import random

CHOICES = ["rock", "paper", "scissors"]

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    return "player" if wins[player] == computer else "computer"

def main():
    print("✊ ✋ ✌ Rock Paper Scissors")
    player_score = 0
    computer_score = 0

    while True:
        player = input("Choose rock, paper, scissors (or q to quit): ").lower()
        if player == "q":
            break
        if player not in CHOICES:
            print("Invalid choice.")
            continue

        computer = random.choice(CHOICES)
        print(f"Computer chose: {computer}")

        result = decide_winner(player, computer)
        if result == "draw":
            print("It's a draw.")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins.")
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score}")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
