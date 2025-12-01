import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "kanban.json"
COLUMNS = ["todo", "doing", "done"]

@dataclass
class Task:
    title: str
    column: str = "todo"

def load_tasks() -> List[Task]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task(**t) for t in data]

def save_tasks(tasks: List[Task]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2)

def list_board(tasks: List[Task]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    for col in COLUMNS:
        print(f"\n== {col.upper()} ==")
        for i, t in enumerate(tasks):
            if t.column == col:
                print(f"- ({i+1}) {t.title}")

def add_task(tasks: List[Task]) -> None:
    title = input("Task title: ").strip()
    if not title:
        print("Title required.")
        return
    tasks.append(Task(title=title))
    save_tasks(tasks)
    print("Task added.")

def move_task(tasks: List[Task]) -> None:
    list_board(tasks)
    idx_str = input("Task number to move: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(tasks)):
        print("Out of range.")
        return
    print("Columns:", ", ".join(COLUMNS))
    col = input("Move to column: ").strip().lower()
    if col not in COLUMNS:
        print("Unknown column.")
        return
    tasks[idx].column = col
    save_tasks(tasks)
    print("Moved.")

def delete_task(tasks: List[Task]) -> None:
    list_board(tasks)
    idx_str = input("Task number to delete: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(tasks)):
        print("Out of range.")
        return
    tasks.pop(idx)
    save_tasks(tasks)
    print("Deleted.")

def main():
    tasks = load_tasks()
    while True:
        print("\nKanban Board CLI")
        print("1. View board")
        print("2. Add task")
        print("3. Move task")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_board(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            move_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
