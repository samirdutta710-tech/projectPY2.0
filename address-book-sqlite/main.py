import sqlite3
from pathlib import Path

DB_PATH = "address_book.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    if not name:
        print("Name required.")
        return
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts(name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added.")

def list_contacts():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, email FROM contacts ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("No contacts.")
        return
    for cid, name, phone, email in rows:
        print(f"{cid}. {name} - {phone} - {email}")

def search_contacts():
    term = input("Search term: ").strip()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, email FROM contacts WHERE name LIKE ?", (f"%{term}%",))
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("No matches.")
        return
    for cid, name, phone, email in rows:
        print(f"{cid}. {name} - {phone} - {email}")

def main():
    init_db()
    while True:
        print("\nAddress Book (SQLite)")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Search")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
