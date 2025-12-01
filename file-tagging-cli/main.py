import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "tags.json"

@dataclass
class FileTag:
    path: str
    tags: List[str]

def load_data() -> List[FileTag]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [FileTag(**d) for d in data]

def save_data(entries: List[FileTag]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in entries], f, indent=2)

def add_tag(entries: List[FileTag]):
    path = input("File path: ").strip()
    if not path:
        print("Path required.")
        return
    tags_str = input("Tags (comma separated): ").strip()
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    if not tags:
        print("No tags given.")
        return

    for e in entries:
        if e.path == path:
            e.tags = sorted(list(set(e.tags + tags)))
            break
    else:
        entries.append(FileTag(path=path, tags=sorted(tags)))

    save_data(entries)
    print("Tags saved.")

def list_all(entries: List[FileTag]):
    if not entries:
        print("No tagged files.")
        return
    for e in entries:
        print(f"{e.path} -> {', '.join(e.tags)}")

def search_by_tag(entries: List[FileTag]):
    tag = input("Tag to search: ").strip().lower()
    results = [e for e in entries if tag in (t.lower() for t in e.tags)]
    if not results:
        print("No files with that tag.")
        return
    for e in results:
        print(f"{e.path} -> {', '.join(e.tags)}")

def main():
    entries = load_data()
    while True:
        print("\nFile Tagging CLI")
        print("1. List tagged files")
        print("2. Add/update tags for file")
        print("3. Search by tag")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_all(entries)
        elif choice == "2":
            add_tag(entries)
        elif choice == "3":
            search_by_tag(entries)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
