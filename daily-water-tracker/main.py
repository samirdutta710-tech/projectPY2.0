import json
import os
from dataclasses import dataclass, asdict
from datetime import date
from typing import List

FILE_NAME = "water_log.json"

@dataclass
class WaterEntry:
    day: str  # ISO date
    glasses: int

def load_entries() -> List[WaterEntry]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [WaterEntry(**e) for e in data]

def save_entries(entries: List[WaterEntry]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in entries], f, indent=2)

def add_today(entries: List[WaterEntry]):
    today = date.today().isoformat()
    glasses_str = input("How many glasses today? ").strip()
    if not glasses_str.isdigit():
        print("Must be a whole number.")
        return
    glasses = int(glasses_str)
    for e in entries:
        if e.day == today:
            e.glasses += glasses
            break
    else:
        entries.append(WaterEntry(day=today, glasses=glasses))
    save_entries(entries)
    print("Updated.")

def show_summary(entries: List[WaterEntry]):
    if not entries:
        print("No entries yet.")
        return
    total = sum(e.glasses for e in entries)
    print(f"\nTotal glasses logged: {total}")
    print("By day:")
    for e in sorted(entries, key=lambda x: x.day):
        print(f"- {e.day}: {e.glasses} glasses")

def main():
    entries = load_entries()
    while True:
        print("\nDaily Water Tracker")
        print("1. Add glasses for today")
        print("2. Show summary")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_today(entries)
        elif choice == "2":
            show_summary(entries)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
