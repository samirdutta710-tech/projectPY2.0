import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "my_quiz.json"

@dataclass
class Question:
    text: str
    options: List[str]
    answer_index: int

def load_questions() -> List[Question]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Question(**q) for q in data]

def save_questions(questions: List[Question]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(q) for q in questions], f, indent=2)

def add_question(questions: List[Question]):
    text = input("Question text: ").strip()
    if not text:
        print("Text required.")
        return
    options = []
    print("Enter options (at least 2). Empty line to stop:")
    while True:
        opt = input(f"Option {len(options)+1}: ").strip()
        if not opt:
            break
        options.append(opt)
    if len(options) < 2:
        print("Need at least 2 options.")
        return
    ans_str = input("Correct option number: ").strip()
    if not ans_str.isdigit():
        print("Invalid number.")
        return
    ans_idx = int(ans_str) - 1
    if not (0 <= ans_idx < len(options)):
        print("Out of range.")
        return
    questions.append(Question(text=text, options=options, answer_index=ans_idx))
    save_questions(questions)
    print("Question added.")

def take_quiz(questions: List[Question]):
    if not questions:
        print("No questions yet.")
        return
    import random
    q_order = questions[:]
    random.shuffle(q_order)
    score = 0
    for q in q_order:
        print("\n" + q.text)
        for i, opt in enumerate(q.options, start=1):
            print(f"{i}. {opt}")
        ans = input("Your answer (number): ").strip()
        if ans.isdigit() and int(ans) - 1 == q.answer_index:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. Correct: {q.options[q.answer_index]}")
    print(f"\nFinal score: {score}/{len(q_order)}")

def main():
    questions = load_questions()
    while True:
        print("\nQuiz Builder CLI")
        print("1. Add question")
        print("2. Take quiz")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_question(questions)
        elif choice == "2":
            take_quiz(questions)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
