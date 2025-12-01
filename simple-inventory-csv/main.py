import csv
from pathlib import Path

FILE_NAME = "inventory.csv"

def load_inventory():
    path = Path(FILE_NAME)
    if not path.is_file():
        return {}
    inventory = {}
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 2:
                continue
            name, qty_str = row
            try:
                qty = int(qty_str)
            except ValueError:
                qty = 0
            inventory[name] = qty
    return inventory

def save_inventory(inventory: dict):
    with Path(FILE_NAME).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for name, qty in inventory.items():
            writer.writerow([name, qty])

def list_items(inventory: dict):
    if not inventory:
        print("Inventory empty.")
        return
    for name, qty in inventory.items():
        print(f"{name}: {qty}")

def add_or_update(inventory: dict):
    name = input("Item name: ").strip()
    if not name:
        print("Name required.")
        return
    qty_str = input("Quantity to set: ").strip()
    if not qty_str.lstrip("-").isdigit():
        print("Quantity must be an integer.")
        return
    qty = int(qty_str)
    inventory[name] = qty
    save_inventory(inventory)
    print("Saved.")

def adjust_quantity(inventory: dict):
    name = input("Item name: ").strip()
    if name not in inventory:
        print("Item not found.")
        return
    delta_str = input("Change in quantity (e.g. -2 or 5): ").strip()
    if not delta_str.lstrip("-").isdigit():
        print("Must be an integer.")
        return
    delta = int(delta_str)
    inventory[name] += delta
    save_inventory(inventory)
    print(f"New quantity for {name}: {inventory[name]}")

def main():
    inventory = load_inventory()
    while True:
        print("\nSimple Inventory CSV")
        print("1. List items")
        print("2. Add/Set item quantity")
        print("3. Adjust quantity (+/-)")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_items(inventory)
        elif choice == "2":
            add_or_update(inventory)
        elif choice == "3":
            adjust_quantity(inventory)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
