import random

WORDS = ["python", "github", "variable", "function", "integer", "string", "loop", "project"]

def scramble(word: str) -> str:
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def main():
    print("🔤 Word Scramble Game")
    random.shuffle(WORDS)
    score = 0

    for word in WORDS:
        scrambled = scramble(word)
        print(f"\nScrambled: {scrambled}")
        guess = input("Your guess (or 'q' to quit): ").strip().lower()
        if guess == "q":
            break
        if guess == word:
            print("Correct!")
            score += 1
        else:
            print(f"Nope, it was: {word}")

    print(f"\nGame over. Score: {score}/{len(WORDS)}")

if __name__ == "__main__":
    main()
