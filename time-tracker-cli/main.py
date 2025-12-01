import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional

FILE_NAME = "time_log.json"
DT_FORMAT = "%Y-%m-%d %H:%M:%S"

@dataclass
class Entry:
    task: str
    start: str
    end: Optional[str]  # can be None while running

def load_entries() -> List[Entry]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Entry(**e) for e in data]

def save_entries(entries: List[Entry]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in entries], f, indent=2)

def get_running(entries: List[Entry]) -> Optional[Entry]:
    for e in entries:
        if e.end is None:
            return e
    return None

def start_task(entries: List[Entry]):
    running = get_running(entries)
    if running:
        print(f"Already tracking '{running.task}', stop it first.")
        return
    task = input("Task name: ").strip()
    if not task:
        print("Task required.")
        return
    now = datetime.now().strftime(DT_FORMAT)
    entries.append(Entry(task=task, start=now, end=None))
    save_entries(entries)
    print(f"Started '{task}' at {now}.")

def stop_task(entries: List[Entry]):
    running = get_running(entries)
    if not running:
        print("No task is currently running.")
        return
    now = datetime.now().strftime(DT_FORMAT)
    running.end = now
    save_entries(entries)
    print(f"Stopped '{running.task}' at {now}.")

def show_report(entries: List[Entry]):
    print("\nTime report:")
    totals = {}
    for e in entries:
        if not e.end:
            continue
        start = datetime.strptime(e.start, DT_FORMAT)
        end = datetime.strptime(e.end, DT_FORMAT)
        minutes = (end - start).total_seconds() / 60
        totals[e.task] = totals.get(e.task, 0) + minutes
    if not totals:
        print("No completed entries.")
        return
    for task, mins in totals.items():
        print(f"{task}: {mins:.1f} minutes")

def main():
    entries = load_entries()
    while True:
        print("\nTime Tracker CLI")
        print("1. Start task")
        print("2. Stop current task")
        print("3. Show report")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            start_task(entries)
        elif choice == "2":
            stop_task(entries)
        elif choice == "3":
            show_report(entries)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
