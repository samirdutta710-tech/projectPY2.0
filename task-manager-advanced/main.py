import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List

FILE_NAME = "tasks.json"
DATE_FMT = "%Y-%m-%d"  # e.g. 2025-12-01

@dataclass
class Task:
    title: str
    priority: int      # 1–5
    due_date: str      # ISO date string
    status: str        # "todo", "doing", "done"

def load_tasks() -> List[Task]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task(**t) for t in data]

def save_tasks(tasks: List[Task]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tasks], f, indent=2)

def add_task(tasks: List[Task]):
    title = input("Title: ").strip()
    if not title:
        print("Title required.")
        return
    try:
        prio = int(input("Priority (1-5, default 3): ") or "3")
    except ValueError:
        prio = 3
    prio = max(1, min(5, prio))
    due = input("Due date (YYYY-MM-DD, optional): ").strip()
    if due:
        try:
            datetime.strptime(due, DATE_FMT)
        except ValueError:
            print("Invalid date, using no due date.")
            due = ""
    status = "todo"
    tasks.append(Task(title=title, priority=prio, due_date=due, status=status))
    save_tasks(tasks)
    print("Task added.")

def list_tasks(tasks: List[Task]):
    if not tasks:
        print("No tasks.")
        return
    sort_key = input("Sort by (p=priority, d=due, s=status, default priority): ").strip().lower() or "p"
    if sort_key == "d":
        tasks_sorted = sorted(tasks, key=lambda t: (t.due_date or "9999-12-31", -t.priority))
    elif sort_key == "s":
        tasks_sorted = sorted(tasks, key=lambda t: t.status)
    else:
        tasks_sorted = sorted(tasks, key=lambda t: -t.priority)
    for i, t in enumerate(tasks_sorted, start=1):
        print(f"{i}. [{t.status}] (prio {t.priority}) {t.title} "
              f"{'due ' + t.due_date if t.due_date else ''}")

def change_status(tasks: List[Task]):
    list_tasks(tasks)
    idx_str = input("Task number: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(tasks)):
        print("Out of range.")
        return
    new_status = input("New status (todo/doing/done): ").strip()
    if new_status not in {"todo", "doing", "done"}:
        print("Invalid status.")
        return
    tasks[idx].status = new_status
    save_tasks(tasks)
    print("Status updated.")

def main():
    tasks = load_tasks()
    while True:
        print("\nAdvanced Task Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Change status")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            change_status(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
