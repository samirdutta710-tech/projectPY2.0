import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "snippets.json"

@dataclass
class Snippet:
    title: str
    tags: List[str]
    body: str

def load_snippets() -> List[Snippet]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Snippet(**s) for s in data]

def save_snippets(snippets: List[Snippet]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(s) for s in snippets], f, indent=2)

def add_snippet(snippets: List[Snippet]):
    title = input("Title: ").strip()
    tags_str = input("Tags (comma separated): ").strip()
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    print("Enter snippet body (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    body = "\n".join(lines)
    snippets.append(Snippet(title=title, tags=tags, body=body))
    save_snippets(snippets)
    print("Snippet saved.")

def list_snippets(snippets: List[Snippet]):
    if not snippets:
        print("No snippets yet.")
        return
    for i, s in enumerate(snippets, start=1):
        print(f"{i}. {s.title} [{', '.join(s.tags)}]")

def search(snippets: List[Snippet]):
    term = input("Search term (tag or text): ").strip().lower()
    matches = []
    for s in snippets:
        if any(term in t.lower() for t in s.tags) or term in s.title.lower() or term in s.body.lower():
            matches.append(s)
    if not matches:
        print("No matches.")
        return
    for s in matches:
        print(f"\n== {s.title} ==")
        print(f"Tags: {', '.join(s.tags)}")
        print(s.body)

def main():
    snippets = load_snippets()
    while True:
        print("\nSnippets Manager")
        print("1. List snippets")
        print("2. Add snippet")
        print("3. Search")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_snippets(snippets)
        elif choice == "2":
            add_snippet(snippets)
        elif choice == "3":
            search(snippets)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
