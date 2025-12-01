from pathlib import Path

FILE_NAME = "shopping_list.txt"

def load_items():
    path = Path(FILE_NAME)
    if not path.is_file():
        return []
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if " | " in line:
            name, qty = line.split(" | ", 1)
            items.append((name, qty))
    return items

def save_items(items):
    lines = [f"{name} | {qty}" for name, qty in items]
    Path(FILE_NAME).write_text("\n".join(lines), encoding="utf-8")

def list_items(items):
    if not items:
        print("Shopping list is empty.")
        return
    for i, (name, qty) in enumerate(items, start=1):
        print(f"{i}. {name} (x{qty})")

def add_item(items):
    name = input("Item name: ").strip()
    if not name:
        print("Name required.")
        return
    qty = input("Quantity (default 1): ").strip() or "1"
    items.append((name, qty))
    save_items(items)
    print("Item added.")

def remove_item(items):
    list_items(items)
    idx_str = input("Number to remove: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(items)):
        print("Out of range.")
        return
    removed = items.pop(idx)
    save_items(items)
    print(f"Removed {removed[0]}.")

def main():
    items = load_items()
    while True:
        print("\nShopping List CLI")
        print("1. View list")
        print("2. Add item")
        print("3. Remove item")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_items(items)
        elif choice == "2":
            add_item(items)
        elif choice == "3":
            remove_item(items)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
