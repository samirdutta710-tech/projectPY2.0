import sqlite3

DB_PATH = "inventory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            location TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_item():
    name = input("Item name: ").strip()
    qty_str = input("Quantity: ").strip()
    location = input("Location: ").strip()
    if not qty_str.isdigit():
        print("Quantity must be a number.")
        return
    qty = int(qty_str)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO items(name, quantity, location) VALUES (?, ?, ?)",
                (name, qty, location))
    conn.commit()
    conn.close()
    print("Item added.")

def list_items():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, quantity, location FROM items ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        print("No items.")
        return
    for i, name, qty, loc in rows:
        print(f"{i}. {name} - {qty} ({loc})")

def update_quantity():
    list_items()
    item_id = input("Item ID to update: ").strip()
    if not item_id.isdigit():
        print("Invalid ID.")
        return
    new_q = input("New quantity: ").strip()
    if not new_q.isdigit():
        print("Invalid quantity.")
        return
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE items SET quantity=? WHERE id=?", (int(new_q), int(item_id)))
    conn.commit()
    conn.close()
    print("Updated.")

def delete_item():
    list_items()
    item_id = input("Item ID to delete: ").strip()
    if not item_id.isdigit():
        print("Invalid ID.")
        return
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id=?", (int(item_id),))
    conn.commit()
    conn.close()
    print("Deleted.")

def main():
    init_db()
    while True:
        print("\nInventory Manager (SQLite)")
        print("1. List items")
        print("2. Add item")
        print("3. Update quantity")
        print("4. Delete item")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
