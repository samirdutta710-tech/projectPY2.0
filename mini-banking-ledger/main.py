import json
import os
from dataclasses import dataclass, asdict
from typing import Dict

FILE_NAME = "accounts.json"

@dataclass
class Account:
    name: str
    balance: float = 0.0

def load_accounts() -> Dict[str, Account]:
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return {name: Account(name=name, balance=bal) for name, bal in data.items()}

def save_accounts(accounts: Dict[str, Account]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump({name: acc.balance for name, acc in accounts.items()}, f, indent=2)

def get_or_create(accounts: Dict[str, Account], name: str) -> Account:
    if name not in accounts:
        accounts[name] = Account(name=name, balance=0.0)
    return accounts[name]

def deposit(accounts: Dict[str, Account]):
    name = input("Account name: ").strip()
    try:
        amount = float(input("Amount to deposit: "))
    except ValueError:
        print("Invalid amount.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    acc = get_or_create(accounts, name)
    acc.balance += amount
    save_accounts(accounts)
    print(f"New balance for {name}: {acc.balance:.2f}")

def withdraw(accounts: Dict[str, Account]):
    name = input("Account name: ").strip()
    try:
        amount = float(input("Amount to withdraw: "))
    except ValueError:
        print("Invalid amount.")
        return
    acc = accounts.get(name)
    if not acc:
        print("No such account.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    if amount > acc.balance:
        print("Insufficient funds.")
        return
    acc.balance -= amount
    save_accounts(accounts)
    print(f"New balance for {name}: {acc.balance:.2f}")

def transfer(accounts: Dict[str, Account]):
    src = input("From account: ").strip()
    dst = input("To account: ").strip()
    try:
        amount = float(input("Amount to transfer: "))
    except ValueError:
        print("Invalid amount.")
        return
    src_acc = accounts.get(src)
    if not src_acc:
        print("Source account does not exist.")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    if amount > src_acc.balance:
        print("Insufficient funds.")
        return
    dst_acc = get_or_create(accounts, dst)
    src_acc.balance -= amount
    dst_acc.balance += amount
    save_accounts(accounts)
    print(f"Transferred {amount:.2f} from {src} to {dst}.")

def list_accounts(accounts: Dict[str, Account]):
    if not accounts:
        print("No accounts yet.")
        return
    for name, acc in accounts.items():
        print(f"{name}: {acc.balance:.2f}")

def main():
    accounts = load_accounts()
    while True:
        print("\nMini Banking Ledger")
        print("1. List accounts")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_accounts(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            transfer(accounts)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
