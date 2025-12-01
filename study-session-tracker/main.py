import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "study_sessions.json"

@dataclass
class Session:
    subject: str
    minutes: int

def load_sessions() -> List[Session]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Session(**s) for s in data]

def save_sessions(sessions: List[Session]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(s) for s in sessions], f, indent=2)

def add_session(sessions: List[Session]):
    subject = input("Subject: ").strip()
    mins_str = input("Minutes studied: ").strip()
    if not mins_str.isdigit():
        print("Minutes must be a whole number.")
        return
    sessions.append(Session(subject=subject, minutes=int(mins_str)))
    save_sessions(sessions)
    print("Session added.")

def show_summary(sessions: List[Session]):
    if not sessions:
        print("No sessions yet.")
        return
    totals = {}
    for s in sessions:
        totals[s.subject] = totals.get(s.subject, 0) + s.minutes
    print("\nStudy time by subject:")
    for subj, mins in totals.items():
        print(f"- {subj}: {mins} min")

def main():
    sessions = load_sessions()
    while True:
        print("\nStudy Session Tracker")
        print("1. Add session")
        print("2. Show summary")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            show_summary(sessions)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
