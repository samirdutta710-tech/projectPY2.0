import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "bookmarks.json"

@dataclass
class Bookmark:
    title: str
    url: str

def load_bookmarks() -> List[Bookmark]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Bookmark(**b) for b in data]

def save_bookmarks(bookmarks: List[Bookmark]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in bookmarks], f, indent=2)

def list_bookmarks(bookmarks: List[Bookmark]):
    if not bookmarks:
        print("No bookmarks yet.")
        return
    for i, b in enumerate(bookmarks, start=1):
        print(f"{i}. {b.title} -> {b.url}")

def add_bookmark(bookmarks: List[Bookmark]):
    title = input("Title: ").strip()
    url = input("URL: ").strip()
    if not title or not url:
        print("Both title and URL required.")
        return
    bookmarks.append(Bookmark(title=title, url=url))
    save_bookmarks(bookmarks)
    print("Bookmark added.")

def search_bookmarks(bookmarks: List[Bookmark]):
    term = input("Search term: ").strip().lower()
    matches = [b for b in bookmarks if term in b.title.lower() or term in b.url.lower()]
    if not matches:
        print("No matches.")
        return
    for b in matches:
        print(f"{b.title} -> {b.url}")

def main():
    bookmarks = load_bookmarks()
    while True:
        print("\nBookmark Manager")
        print("1. List bookmarks")
        print("2. Add bookmark")
        print("3. Search")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_bookmarks(bookmarks)
        elif choice == "2":
            add_bookmark(bookmarks)
        elif choice == "3":
            search_bookmarks(bookmarks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
