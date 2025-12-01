from datetime import datetime
from pathlib import Path

FILE_NAME = "journal.txt"

def add_entry():
    print("Write your entry (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    entry = "\n".join(lines)
    if not entry.strip():
        print("Empty entry, not saved.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n{entry}\n\n")
    print("Entry saved.")

def view_entries():
    p = Path(FILE_NAME)
    if not p.is_file():
        print("No entries yet.")
        return
    print(p.read_text(encoding="utf-8"))

def main():
    while True:
        print("\nDaily Journal")
        print("1. Add entry")
        print("2. View all entries")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
