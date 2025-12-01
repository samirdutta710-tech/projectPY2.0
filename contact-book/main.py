import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)

def list_contacts(contacts):
    if not contacts:
        print("No contacts.")
        return
    for c in contacts:
        print(f"{c['name']} - {c['phone']} - {c['email']}")

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added.")

def search_contacts(contacts):
    term = input("Search term: ").lower()
    results = [c for c in contacts if term in c["name"].lower()]
    if not results:
        print("No matches.")
    else:
        for c in results:
            print(f"{c['name']} - {c['phone']} - {c['email']}")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Book")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Search contacts")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
