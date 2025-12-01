import json
import os
from dataclasses import dataclass, asdict
from datetime import date, timedelta
from typing import List

FILE_NAME = "habits.json"

@dataclass
class Habit:
    name: str
    days_done: List[str]  # list of ISO dates

def load_habits() -> List[Habit]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Habit(**h) for h in data]

def save_habits(habits: List[Habit]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(h) for h in habits], f, indent=2)

def add_habit(habits: List[Habit]):
    name = input("Habit name: ").strip()
    if not name:
        print("Name required.")
        return
    habits.append(Habit(name=name, days_done=[]))
    save_habits(habits)
    print("Habit added.")

def mark_today(habits: List[Habit]):
    if not habits:
        print("No habits.")
        return
    today = date.today().isoformat()
    for i, h in enumerate(habits, start=1):
        print(f"{i}. {h.name}")
    idx_str = input("Which habit did you complete today? (number): ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(habits)):
        print("Out of range.")
        return
    h = habits[idx]
    if today not in h.days_done:
        h.days_done.append(today)
        save_habits(habits)
        print("Marked as done for today.")
    else:
        print("Already marked for today.")

def calc_streak(days_done: List[str]) -> int:
    if not days_done:
        return 0
    days = sorted(date.fromisoformat(d) for d in days_done)
    streak = 1
    best = 1
    for i in range(1, len(days)):
        if days[i] == days[i-1] + timedelta(days=1):
            streak += 1
            best = max(best, streak)
        elif days[i] == days[i-1]:
            continue
        else:
            streak = 1
    return best

def show_stats(habits: List[Habit]):
    if not habits:
        print("No habits.")
        return
    print("\nHabit stats:")
    for h in habits:
        best = calc_streak(h.days_done)
        total = len(set(h.days_done))
        print(f"- {h.name}: {total} days done, best streak {best}")

def main():
    habits = load_habits()
    while True:
        print("\nCLI Habit Tracker")
        print("1. Add habit")
        print("2. Mark today as done")
        print("3. Show stats")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_today(habits)
        elif choice == "3":
            show_stats(habits)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
