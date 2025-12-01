import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "splits.json"

@dataclass
class Expense:
    description: str
    total: float
    people: List[str]

def load_expenses() -> List[Expense]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Expense(**e) for e in data]

def save_expenses(expenses: List[Expense]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in expenses], f, indent=2)

def add_expense(expenses: List[Expense]) -> None:
    desc = input("Description: ").strip()
    try:
        total = float(input("Total amount: "))
    except ValueError:
        print("Invalid amount.")
        return
    people_str = input("People involved (comma separated): ")
    people = [p.strip() for p in people_str.split(",") if p.strip()]
    if not people:
        print("Need at least 1 person.")
        return
    expenses.append(Expense(description=desc, total=total, people=people))
    save_expenses(expenses)
    print("Expense added.")

def show_expenses(expenses: List[Expense]) -> None:
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        per_person = e.total / len(e.people)
        print(f"{i}. {e.description}: ${e.total:.2f} -> {len(e.people)} people, ${per_person:.2f} each")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Splitter")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
