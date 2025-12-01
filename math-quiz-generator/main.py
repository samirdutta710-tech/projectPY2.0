import random
import json
import os
from dataclasses import dataclass, asdict

SCORES_FILE = "math_quiz_scores.json"

@dataclass
class ScoreEntry:
    name: str
    score: int
    total: int

def generate_question():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        answer = a + b
    elif op == "-":
        answer = a - b
    else:
        answer = a * b
    question = f"{a} {op} {b} = ? "
    return question, answer

def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [ScoreEntry(**d) for d in data]

def save_scores(scores):
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(s) for s in scores], f, indent=2)

def show_high_scores(scores):
    if not scores:
        print("No scores yet.")
        return
    sorted_scores = sorted(scores, key=lambda s: s.score, reverse=True)[:10]
    print("\nHigh Scores:")
    for s in sorted_scores:
        print(f"{s.name}: {s.score}/{s.total}")

def main():
    name = input("Enter your name: ").strip() or "Player"
    num_q_str = input("How many questions? (default 5): ").strip()
    num_q = int(num_q_str) if num_q_str.isdigit() else 5

    score = 0
    for _ in range(num_q):
        question, answer = generate_question()
        try:
            user_ans = int(input(question))
            if user_ans == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong, correct answer was {answer}")
        except ValueError:
            print(f"Invalid input, correct answer was {answer}")

    print(f"\n{name}, you scored {score}/{num_q}")
    scores = load_scores()
    scores.append(ScoreEntry(name=name, score=score, total=num_q))
    save_scores(scores)
    show_high_scores(scores)

if __name__ == "__main__":
    main()
