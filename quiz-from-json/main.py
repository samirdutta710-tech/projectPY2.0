import json
import os
import random
from dataclasses import dataclass
from typing import List

FILE_NAME = "questions.json"

@dataclass
class Question:
    question: str
    options: List[str]
    answer_index: int  # index into options list

DEFAULT_QUESTIONS = [
    {
        "question": "What is the output of 3 * 2 ** 2?",
        "options": ["12", "18", "9", "6"],
        "answer_index": 0,
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "fn"],
        "answer_index": 2,
    },
]

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_QUESTIONS, f, indent=2)

def load_questions() -> List[Question]:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Question(**q) for q in data]

def run_quiz(questions: List[Question]):
    random.shuffle(questions)
    score = 0
    for q in questions:
        print("\n" + q.question)
        for i, opt in enumerate(q.options, start=1):
            print(f"{i}. {opt}")
        ans = input("Your answer (number): ").strip()
        if ans.isdigit():
            idx = int(ans) - 1
            if idx == q.answer_index:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. Correct: {q.options[q.answer_index]}")
        else:
            print("Invalid input.")
    print(f"\nFinal score: {score}/{len(questions)}")

def main():
    init_file()
    questions = load_questions()
    print("JSON Quiz Engine")
    run_quiz(questions)

if __name__ == "__main__":
    main()
