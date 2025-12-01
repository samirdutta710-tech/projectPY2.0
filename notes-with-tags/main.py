import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "notes.json"

@dataclass
class Note:
    title: str
    body: str
    tags: List[str]

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Note(**n) for n in data]

def save_notes(notes):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(n) for n in notes], f, indent=2)

def list_notes(notes):
    if not notes:
        print("No notes yet.")
        return
    for i, note in enumerate(notes, start=1):
        tags = ", ".join(note.tags)
        print(f"{i}. {note.title} [{tags}]")

def add_note(notes):
    title = input("Title: ")
    print("Body (end with empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    body = "\n".join(lines)
    tags_str = input("Tags (comma-separated): ")
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    notes.append(Note(title=title, body=body, tags=tags))
    save_notes(notes)
    print("Note added.")

def search_by_tag(notes):
    tag = input("Tag to search: ").strip().lower()
    results = [n for n in notes if tag in (t.lower() for t in n.tags)]
    if not results:
        print("No notes with that tag.")
        return
    for note in results:
        print(f"\n{note.title} [{', '.join(note.tags)}]")
        print("-" * len(note.title))
        print(note.body)

def main():
    notes = load_notes()
    while True:
        print("\nNotes with Tags")
        print("1. List notes")
        print("2. Add note")
        print("3. Search by tag")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_notes(notes)
        elif choice == "2":
            add_note(notes)
        elif choice == "3":
            search_by_tag(notes)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
