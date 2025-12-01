import random

def play_game():
    print("🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")

        if guess.lower() == 'q':
            print("Goodbye!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"🎉 You got it in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()
