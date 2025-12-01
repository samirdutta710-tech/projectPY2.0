import time

TEST_SENTENCES = [
    "Python makes programming fun and productive.",
    "Practice every day to become a better developer.",
    "Typing speed tests can help improve your skills.",
]

def calculate_wpm(chars_typed: int, seconds: float) -> float:
    words = chars_typed / 5  # standard WPM definition
    minutes = seconds / 60
    if minutes == 0:
        return 0.0
    return words / minutes

def accuracy(original: str, typed: str) -> float:
    correct = 0
    for o, t in zip(original, typed):
        if o == t:
            correct += 1
    if len(original) == 0:
        return 0.0
    return correct / len(original) * 100

def main():
    import random
    sentence = random.choice(TEST_SENTENCES)
    print("💻 Typing Speed Tester\n")
    print("Type this sentence exactly and press Enter:\n")
    print(sentence)
    input("\nPress Enter when you're ready...")

    start = time.time()
    typed = input("\nStart typing: ")
    end = time.time()

    elapsed = end - start
    wpm = calculate_wpm(len(typed), elapsed)
    acc = accuracy(sentence, typed)

    print(f"\nTime: {elapsed:.2f} seconds")
    print(f"WPM : {wpm:.1f}")
    print(f"Accuracy: {acc:.1f}%")

if __name__ == "__main__":
    main()
