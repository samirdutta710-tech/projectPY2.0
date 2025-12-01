import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "notes.json"

@dataclass
class Note:
    title: str
    tags: List[str]
    body: str

def load_notes() -> List[Note]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Note(**n) for n in data]

def save_notes(notes: List[Note]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(n) for n in notes], f, indent=2)

def add_note(notes: List[Note]):
    title = input("Title: ").strip()
    tags_str = input("Tags (comma separated): ").strip()
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    print("Enter markdown body (empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    body = "\n".join(lines)
    notes.append(Note(title=title, tags=tags, body=body))
    save_notes(notes)
    print("Note added.")

def list_notes(notes: List[Note]):
    if not notes:
        print("No notes yet.")
        return
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n.title} [{', '.join(n.tags)}]")

def view_note(notes: List[Note]):
    list_notes(notes)
    idx_str = input("Note number: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(notes)):
        print("Out of range.")
        return
    n = notes[idx]
    print(f"\n# {n.title}\nTags: {', '.join(n.tags)}\n")
    print(n.body)

def search_notes(notes: List[Note]):
    term = input("Search term (title/tag/text): ").strip().lower()
    results = []
    for n in notes:
        if term in n.title.lower() or term in n.body.lower() or any(term in t.lower() for t in n.tags):
            results.append(n)
    if not results:
        print("No matches.")
        return
    for n in results:
        print(f"- {n.title} [{', '.join(n.tags)}]")

def main():
    notes = load_notes()
    while True:
        print("\nMarkdown Notes with Tags")
        print("1. List notes")
        print("2. Add note")
        print("3. View note")
        print("4. Search notes")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            view_note(notes)
        elif choice == "4":
            search_notes(notes)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
