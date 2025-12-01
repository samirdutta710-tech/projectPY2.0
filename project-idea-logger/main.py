import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "ideas.json"

@dataclass
class Idea:
    title: str
    description: str
    status: str      # "todo", "in-progress", "done"
    priority: int    # 1-5

def load_ideas() -> List[Idea]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Idea(**d) for d in data]

def save_ideas(ideas: List[Idea]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(i) for i in ideas], f, indent=2)

def list_ideas(ideas: List[Idea]):
    if not ideas:
        print("No ideas yet.")
        return
    sorted_ideas = sorted(ideas, key=lambda i: (i.status, -i.priority))
    for idx, i in enumerate(sorted_ideas, start=1):
        print(f"{idx}. [{i.status}] (prio {i.priority}) {i.title}")
        print(f"   {i.description}")

def add_idea(ideas: List[Idea]):
    title = input("Title: ").strip()
    desc = input("Description: ").strip()
    status = input("Status (todo/in-progress/done, default todo): ").strip() or "todo"
    try:
        prio = int(input("Priority 1-5 (default 3): ") or "3")
    except ValueError:
        prio = 3
    prio = max(1, min(5, prio))
    ideas.append(Idea(title=title, description=desc, status=status, priority=prio))
    save_ideas(ideas)
    print("Idea added.")

def change_status(ideas: List[Idea]):
    list_ideas(ideas)
    idx_str = input("Idea number to update: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(ideas)):
        print("Out of range.")
        return
    new_status = input("New status (todo/in-progress/done): ").strip()
    if new_status not in {"todo", "in-progress", "done"}:
        print("Invalid status.")
        return
    ideas[idx].status = new_status
    save_ideas(ideas)
    print("Updated.")

def main():
    ideas = load_ideas()
    while True:
        print("\nProject Idea Logger")
        print("1. List ideas")
        print("2. Add idea")
        print("3. Change idea status")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_ideas(ideas)
        elif choice == "2":
            add_idea(ideas)
        elif choice == "3":
            change_status(ideas)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
