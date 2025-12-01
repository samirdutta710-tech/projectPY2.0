import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime

FILE_NAME = "tasks.json"
DATE_FORMAT = "%Y-%m-%d"

@dataclass
class Task:
    title: str
    due_date: str  # ISO date string
    done: bool = False

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task(**t) for t in data]

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    today = datetime.today().date()
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t.done else "❌"
        try:
            due = datetime.strptime(t.due_date, DATE_FORMAT).date()
            overdue = (not t.done) and due < today
            flag = " (OVERDUE)" if overdue else ""
        except ValueError:
            flag = ""
        print(f"{i}. {t.title} - due {t.due_date} {status}{flag}")

def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Title required.")
        return
    due = input("Due date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(due, DATE_FORMAT)
    except ValueError:
        print("Invalid date format.")
        return
    tasks.append(Task(title=title, due_date=due))
    save_tasks(tasks)
    print("Task added.")

def toggle_task(tasks):
    list_tasks(tasks)
    choice = input("Task number to toggle done/undone: ").strip()
    if not choice.isdigit():
        print("Invalid number.")
        return
    idx = int(choice) - 1
    if not (0 <= idx < len(tasks)):
        print("Out of range.")
        return
    tasks[idx].done = not tasks[idx].done
    save_tasks(tasks)
    print("Updated.")

def main():
    tasks = load_tasks()
    while True:
        print("\nJSON To-Do with Deadlines")
        print("1. List tasks")
        print("2. Add task")
        print("3. Toggle done")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
