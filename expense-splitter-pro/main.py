import json
import os
from dataclasses import dataclass, asdict
from typing import List, Dict

FILE_NAME = "expenses.json"

@dataclass
class Expense:
    payer: str
    amount: float
    description: str
    participants: List[str]  # people sharing this expense

def load_expenses() -> List[Expense]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Expense(**e) for e in data]

def save_expenses(expenses: List[Expense]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in expenses], f, indent=2)

def add_expense(expenses: List[Expense]):
    payer = input("Who paid? ").strip()
    amt_str = input("Amount: ").strip()
    desc = input("Description: ").strip()
    people_str = input("Participants (comma separated): ").strip()
    try:
        amount = float(amt_str)
    except ValueError:
        print("Invalid amount.")
        return
    participants = [p.strip() for p in people_str.split(",") if p.strip()]
    if not payer or not participants:
        print("Payer and participants required.")
        return
    expenses.append(Expense(payer=payer, amount=amount,
                            description=desc, participants=participants))
    save_expenses(expenses)
    print("Expense added.")

def list_expenses(expenses: List[Expense]):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        parts = ", ".join(e.participants)
        print(f"{i}. {e.description} - {e.amount:.2f} paid by {e.payer} (shared by {parts})")

def compute_balances(expenses: List[Expense]):
    balances: Dict[str, float] = {}
    for e in expenses:
        share = e.amount / len(e.participants)
        # each participant owes their share
        for p in e.participants:
            balances[p] = balances.get(p, 0.0) - share
        # payer gets the full amount back
        balances[e.payer] = balances.get(e.payer, 0.0) + e.amount

    print("\nNet balances (positive = others owe them, negative = they owe):")
    for person, bal in balances.items():
        print(f"- {person}: {bal:.2f}")

    # Suggest simple settlements (greedy)
    creditors = [(p, bal) for p, bal in balances.items() if bal > 0]
    debtors = [(p, -bal) for p, bal in balances.items() if bal < 0]
    creditors.sort(key=lambda x: -x[1])
    debtors.sort(key=lambda x: -x[1])

    print("\nSuggested settlements:")
    i = j = 0
    while i < len(debtors) and j < len(creditors):
        d_name, d_amt = debtors[i]
        c_name, c_amt = creditors[j]
        pay = min(d_amt, c_amt)
        print(f"- {d_name} pays {c_name} {pay:.2f}")
        d_amt -= pay
        c_amt -= pay
        if d_amt == 0:
            i += 1
        else:
            debtors[i] = (d_name, d_amt)
        if c_amt == 0:
            j += 1
        else:
            creditors[j] = (c_name, c_amt)

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Splitter Pro")
        print("1. List expenses")
        print("2. Add expense")
        print("3. Compute balances & settlements")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_expenses(expenses)
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            compute_balances(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
