import json
import os
from dataclasses import dataclass, asdict
from datetime import date
from typing import List

FILE_NAME = "budget.json"

@dataclass
class Entry:
    kind: str      # "income" or "expense"
    amount: float
    category: str
    date: str      # ISO

def load_entries() -> List[Entry]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Entry(**e) for e in data]

def save_entries(entries: List[Entry]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in entries], f, indent=2)

def add_entry(entries: List[Entry], kind: str):
    amount_str = input("Amount: ").strip()
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid amount.")
        return
    category = input("Category: ").strip() or "general"
    entries.append(Entry(kind=kind, amount=amount, category=category, date=date.today().isoformat()))
    save_entries(entries)
    print("Added.")

def show_summary(entries: List[Entry]):
    income = sum(e.amount for e in entries if e.kind == "income")
    expenses = sum(e.amount for e in entries if e.kind == "expense")
    balance = income - expenses
    print(f"\nIncome:  {income:.2f}")
    print(f"Expense: {expenses:.2f}")
    print(f"Balance: {balance:.2f}")

    category_totals = {}
    for e in entries:
        category_totals.setdefault(e.category, 0.0)
        if e.kind == "expense":
            category_totals[e.category] += e.amount
    if category_totals:
        print("\nExpenses by category:")
        for cat, amt in category_totals.items():
            print(f"- {cat}: {amt:.2f}")

def list_entries(entries: List[Entry]):
    if not entries:
        print("No entries yet.")
        return
    for e in entries:
        sign = "+" if e.kind == "income" else "-"
        print(f"{e.date} {sign}{e.amount:.2f} [{e.category}]")

def main():
    entries = load_entries()
    while True:
        print("\nBudget Planner")
        print("1. Add income")
        print("2. Add expense")
        print("3. List entries")
        print("4. Show summary")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_entry(entries, "income")
        elif choice == "2":
            add_entry(entries, "expense")
        elif choice == "3":
            list_entries(entries)
        elif choice == "4":
            show_summary(entries)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
