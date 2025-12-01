import json
import os
from dataclasses import dataclass, asdict
from datetime import date

FILE_NAME = "habits.json"

@dataclass
class Habit:
    name: str
    log: list[str]  # list of ISO date strings

def load_habits() -> list[Habit]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Habit(**h) for h in data]

def save_habits(habits: list[Habit]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(h) for h in habits], f, indent=2)

def list_habits(habits: list[Habit]) -> None:
    if not habits:
        print("No habits yet. Add one!")
        return
    for i, h in enumerate(habits, start=1):
        print(f"{i}. {h.name} (entries: {len(h.log)})")

def add_habit(habits: list[Habit]) -> None:
    name = input("Habit name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    habits.append(Habit(name=name, log=[]))
    save_habits(habits)
    print("Habit added.")

def mark_today(habits: list[Habit]) -> None:
    if not habits:
        print("No habits to mark.")
        return
    list_habits(habits)
    choice = input("Select habit number to mark for today: ")
    if not choice.isdigit():
        print("Invalid input.")
        return
    idx = int(choice) - 1
    if not (0 <= idx < len(habits)):
        print("Out of range.")
        return
    today = date.today().isoformat()
    if today not in habits[idx].log:
        habits[idx].log.append(today)
        save_habits(habits)
        print("Marked!")
    else:
        print("Already marked for today.")

def show_stats(habits: list[Habit]) -> None:
    if not habits:
        print("No habits.")
        return
    for h in habits:
        print(f"{h.name}: {len(h.log)} days total")

def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracker")
        print("1. List habits")
        print("2. Add habit")
        print("3. Mark today")
        print("4. Show stats")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_habits(habits)
        elif choice == "2":
            add_habit(habits)
        elif choice == "3":
            mark_today(habits)
        elif choice == "4":
            show_stats(habits)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
