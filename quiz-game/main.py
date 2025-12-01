QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is this project written in?",
        "options": ["A) Java", "B) Python", "C) C++", "D) JavaScript"],
        "answer": "B"
    },
]

def ask_question(q):
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    choice = input("Your answer (A/B/C/D): ").upper()
    return choice == q["answer"]

def main():
    print("🧠 Quiz Game")
    score = 0

    for q in QUESTIONS:
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. Correct answer was {q['answer']}.")

    print(f"\nYou scored {score}/{len(QUESTIONS)}")

if __name__ == "__main__":
    main()
