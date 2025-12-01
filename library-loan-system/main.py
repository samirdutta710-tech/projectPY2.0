import json
import os
from dataclasses import dataclass, asdict
from typing import Dict

FILE_NAME = "library.json"

@dataclass
class Book:
    id: str
    title: str
    author: str
    available: bool = True
    borrower: str = ""

@dataclass
class Library:
    books: Dict[str, Book]

def load_library() -> Library:
    if not os.path.exists(FILE_NAME):
        return Library(books={})
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        books = {bid: Book(**b) for bid, b in data.get("books", {}).items()}
        return Library(books=books)

def save_library(lib: Library):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump({"books": {bid: asdict(b) for bid, b in lib.books.items()}}, f, indent=2)

def add_book(lib: Library):
    bid = input("Book ID: ").strip()
    if not bid:
        print("ID required.")
        return
    if bid in lib.books:
        print("Book ID already exists.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    lib.books[bid] = Book(id=bid, title=title, author=author)
    save_library(lib)
    print("Book added.")

def list_books(lib: Library):
    if not lib.books:
        print("No books.")
        return
    for b in lib.books.values():
        status = "Available" if b.available else f"Out (to {b.borrower})"
        print(f"{b.id}: {b.title} - {b.author} [{status}]")

def checkout_book(lib: Library):
    bid = input("Book ID: ").strip()
    borrower = input("Borrower name: ").strip()
    book = lib.books.get(bid)
    if not book:
        print("No such book.")
        return
    if not book.available:
        print("Book already checked out.")
        return
    book.available = False
    book.borrower = borrower
    save_library(lib)
    print("Checked out.")

def return_book(lib: Library):
    bid = input("Book ID: ").strip()
    book = lib.books.get(bid)
    if not book:
        print("No such book.")
        return
    if book.available:
        print("Book is not checked out.")
        return
    book.available = True
    book.borrower = ""
    save_library(lib)
    print("Returned.")

def main():
    lib = load_library()
    while True:
        print("\nLibrary Loan System")
        print("1. List books")
        print("2. Add book")
        print("3. Check out book")
        print("4. Return book")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_books(lib)
        elif choice == "2":
            add_book(lib)
        elif choice == "3":
            checkout_book(lib)
        elif choice == "4":
            return_book(lib)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
