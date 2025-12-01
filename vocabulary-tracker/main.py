import json
import os
import random
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "vocab.json"

@dataclass
class VocabWord:
    word: str
    definition: str
    correct_count: int = 0
    wrong_count: int = 0

def load_words() -> List[VocabWord]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [VocabWord(**w) for w in data]

def save_words(words: List[VocabWord]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(w) for w in words], f, indent=2)

def add_word(words: List[VocabWord]):
    word = input("Word: ").strip()
    definition = input("Definition: ").strip()
    if not word or not definition:
        print("Both required.")
        return
    words.append(VocabWord(word=word, definition=definition))
    save_words(words)
    print("Word added.")

def list_words(words: List[VocabWord]):
    if not words:
        print("No words yet.")
        return
    for w in words:
        print(f"- {w.word}: {w.definition} "
              f"(correct: {w.correct_count}, wrong: {w.wrong_count})")

def quiz(words: List[VocabWord]):
    if not words:
        print("No words to quiz.")
        return
    random.shuffle(words)
    for w in words:
        print("\nDefinition:")
        print(w.definition)
        guess = input("Your guess: ").strip()
        if guess.lower() == w.word.lower():
            print("✅ Correct!")
            w.correct_count += 1
        else:
            print(f"❌ Incorrect. The word was: {w.word}")
            w.wrong_count += 1
        save_words(words)

def stats(words: List[VocabWord]):
    if not words:
        print("No words.")
        return
    print("\nStats:")
    for w in words:
        total = w.correct_count + w.wrong_count
        acc = (w.correct_count / total * 100) if total else 0.0
        print(f"- {w.word}: {w.correct_count}✔ {w.wrong_count}✘ ({acc:.1f}%)")

def main():
    words = load_words()
    while True:
        print("\nVocabulary Tracker")
        print("1. List words")
        print("2. Add word")
        print("3. Quiz")
        print("4. Stats")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_words(words)
        elif choice == "2":
            add_word(words)
        elif choice == "3":
            quiz(words)
        elif choice == "4":
            stats(words)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
