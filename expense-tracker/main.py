import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "note"])

def add_expense():
    amount = input("Amount: ")
    category = input("Category: ")
    note = input("Note: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date.today().isoformat(), amount, category, note])
    print("Expense added.")

def list_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses yet.")
        return

    total = 0.0
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['date']} | ${row['amount']} | {row['category']} | {row['note']}")
            total += float(row["amount"])
    print(f"Total: ${total:.2f}")

def main():
    init_file()
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
