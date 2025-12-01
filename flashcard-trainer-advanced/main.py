import json
import os
import random
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "flashcards.json"

@dataclass
class Card:
    question: str
    answer: str
    correct_count: int = 0
    wrong_count: int = 0

def load_cards() -> List[Card]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Card(**c) for c in data]

def save_cards(cards: List[Card]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(c) for c in cards], f, indent=2)

def add_card(cards: List[Card]):
    q = input("Question: ").strip()
    a = input("Answer: ").strip()
    if not q or not a:
        print("Both required.")
        return
    cards.append(Card(question=q, answer=a))
    save_cards(cards)
    print("Card added.")

def practice(cards: List[Card]):
    if not cards:
        print("No cards yet.")
        return
    random.shuffle(cards)
    for c in cards:
        print("\nQ:", c.question)
        input("Press Enter to show answer...")
        print("A:", c.answer)
        result = input("Did you get it right? (y/n): ").strip().lower()
        if result == "y":
            c.correct_count += 1
        else:
            c.wrong_count += 1
        save_cards(cards)

def stats(cards: List[Card]):
    if not cards:
        print("No cards.")
        return
    print("\nFlashcard Stats:")
    for c in cards:
        total = c.correct_count + c.wrong_count
        if total == 0:
            acc = 0.0
        else:
            acc = c.correct_count / total * 100
        print(f"- {c.question[:30]}... -> {c.correct_count}✔ {c.wrong_count}✘ ({acc:.1f}%)")

def main():
    cards = load_cards()
    while True:
        print("\nFlashcard Trainer Advanced")
        print("1. Add card")
        print("2. Practice")
        print("3. View stats")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_card(cards)
        elif choice == "2":
            practice(cards)
        elif choice == "3":
            stats(cards)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
