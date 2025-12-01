import json
import os
import random
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "vocab.json"

@dataclass
class Word:
    term: str
    meaning: str

def load_words() -> List[Word]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Word(**w) for w in data]

def save_words(words: List[Word]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(w) for w in words], f, indent=2)

def add_word(words: List[Word]):
    term = input("Word: ").strip()
    meaning = input("Meaning: ").strip()
    if not term or not meaning:
        print("Both required.")
        return
    words.append(Word(term=term, meaning=meaning))
    save_words(words)
    print("Added.")

def list_words(words: List[Word]):
    if not words:
        print("No words yet.")
        return
    for w in words:
        print(f"{w.term} - {w.meaning}")

def quiz(words: List[Word]):
    if not words:
        print("No words to quiz.")
        return
    random.shuffle(words)
    score = 0
    for w in words:
        ans = input(f"What does '{w.term}' mean? ").strip().lower()
        if ans == w.meaning.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Meaning: {w.meaning}")
    print(f"Score: {score}/{len(words)}")

def main():
    words = load_words()
    while True:
        print("\nVocabulary Trainer")
        print("1. List words")
        print("2. Add word")
        print("3. Quiz")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_words(words)
        elif choice == "2":
            add_word(words)
        elif choice == "3":
            quiz(words)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
