import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "contacts.json"

@dataclass
class Contact:
    name: str
    phone: str
    group: str  # e.g. "family", "friends", "work"

def load_contacts() -> List[Contact]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Contact(**c) for c in data]

def save_contacts(contacts: List[Contact]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(c) for c in contacts], f, indent=2)

def list_contacts(contacts: List[Contact]):
    if not contacts:
        print("No contacts.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c.name} ({c.group}) - {c.phone}")

def add_contact(contacts: List[Contact]):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    group = input("Group (family/friends/work/etc): ").strip() or "other"
    if not name:
        print("Name required.")
        return
    contacts.append(Contact(name=name, phone=phone, group=group))
    save_contacts(contacts)
    print("Contact added.")

def filter_by_group(contacts: List[Contact]):
    grp = input("Group to filter: ").strip().lower()
    results = [c for c in contacts if c.group.lower() == grp]
    if not results:
        print("No contacts in that group.")
        return
    for c in results:
        print(f"{c.name} - {c.phone}")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Grouper")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Filter by group")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            filter_by_group(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
