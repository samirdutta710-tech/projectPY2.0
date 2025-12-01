import json
import os
import random

FILE_NAME = "flashcards.json"

DEFAULT_FLASHCARDS = [
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "2 + 2 * 2 = ?", "answer": "6"},
    {"question": "What keyword defines a function in Python?", "answer": "def"},
]

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_FLASHCARDS, f, indent=2)

def load_flashcards():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def train(flashcards):
    random.shuffle(flashcards)
    correct = 0

    for card in flashcards:
        print("\nQuestion:", card["question"])
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == card["answer"].lower():
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong. Correct answer: {card['answer']}")

    print(f"\nScore: {correct}/{len(flashcards)} correct.")

def main():
    init_file()
    flashcards = load_flashcards()
    print("Flashcard Trainer")
    train(flashcards)

if __name__ == "__main__":
    main()
