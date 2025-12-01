import calendar
import json
import os
from datetime import date

FILE_NAME = "notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

def show_month(year: int, month: int, notes: dict):
    print("\n", calendar.month_name[month], year)
    cal = calendar.monthcalendar(year, month)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        line = ""
        for day in week:
            if day == 0:
                line += "   "
            else:
                key = f"{year}-{month:02d}-{day:02d}"
                mark = "*" if key in notes else " "
                line += f"{day:2d}{mark}"
            line += " "
        print(line)

def add_note(notes: dict, year: int, month: int):
    day_str = input("Day of month: ").strip()
    if not day_str.isdigit():
        print("Invalid day.")
        return
    day = int(day_str)
    try:
        d = date(year, month, day)
    except ValueError:
        print("Invalid date.")
        return
    key = d.isoformat()
    text = input("Note: ").strip()
    if not text:
        print("Empty note, not saved.")
        return
    notes[key] = text
    save_notes(notes)
    print("Saved.")

def view_notes(notes: dict, year: int, month: int):
    print("\nNotes this month:")
    for key, text in sorted(notes.items()):
        y, m, _ = key.split("-")
        if int(y) == year and int(m) == month:
            print(f"{key}: {text}")

def main():
    today = date.today()
    year = today.year
    month = today.month
    notes = load_notes()

    while True:
        show_month(year, month, notes)
        print("\nCalendar Notes CLI")
        print("1. Add note")
        print("2. View notes this month")
        print("3. Next month")
        print("4. Previous month")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_note(notes, year, month)
        elif choice == "2":
            view_notes(notes, year, month)
        elif choice == "3":
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        elif choice == "4":
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
