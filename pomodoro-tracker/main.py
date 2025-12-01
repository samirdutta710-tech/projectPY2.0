import time
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List

FILE_NAME = "pomodoro_log.json"

@dataclass
class Session:
    started_at: str
    duration_minutes: int
    kind: str  # "work" or "break"

def load_sessions() -> List[Session]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Session(**s) for s in data]

def save_sessions(sessions: List[Session]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(s) for s in sessions], f, indent=2)

def run_timer(minutes: int, kind: str, sessions: List[Session]):
    print(f"Starting {kind} session for {minutes} minutes...")
    seconds = minutes * 60
    start = datetime.now().isoformat(timespec="seconds")
    while seconds > 0:
        m, s = divmod(seconds, 60)
        print(f"{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nSession finished!")
    sessions.append(Session(started_at=start, duration_minutes=minutes, kind=kind))
    save_sessions(sessions)

def show_stats(sessions: List[Session]):
    total_work = sum(s.duration_minutes for s in sessions if s.kind == "work")
    total_break = sum(s.duration_minutes for s in sessions if s.kind == "break")
    print(f"Total work minutes: {total_work}")
    print(f"Total break minutes: {total_break}")
    print(f"Total sessions: {len(sessions)}")

def main():
    sessions = load_sessions()
    while True:
        print("\nPomodoro Tracker")
        print("1. Start work (25 min)")
        print("2. Start break (5 min)")
        print("3. Show stats")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            run_timer(25, "work", sessions)
        elif choice == "2":
            run_timer(5, "break", sessions)
        elif choice == "3":
            show_stats(sessions)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
