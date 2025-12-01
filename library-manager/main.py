import json
import os
from dataclasses import dataclass, asdict

FILE_NAME = "library.json"

@dataclass
class Book:
    title: str
    author: str
    year: int
    read: bool = False

def load_library():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Book(**item) for item in data]

def save_library(books):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, indent=2)

def list_books(books):
    if not books:
        print("No books in library.")
        return
    for i, book in enumerate(books, start=1):
        status = "✅" if book.read else "❌"
        print(f"{i}. {book.title} by {book.author} ({book.year}) [{status}]")

def add_book(books):
    title = input("Title: ")
    author = input("Author: ")
    year_str = input("Year: ")
    try:
        year = int(year_str)
    except ValueError:
        print("Year must be a number.")
        return
    books.append(Book(title=title, author=author, year=year))
    save_library(books)
    print("Book added.")

def mark_read(books):
    list_books(books)
    choice = input("Enter book number to toggle read/unread: ")
    if not choice.isdigit():
        print("Invalid number.")
        return
    idx = int(choice) - 1
    if not (0 <= idx < len(books)):
        print("Out of range.")
        return
    books[idx].read = not books[idx].read
    save_library(books)
    print("Updated.")

def main():
    books = load_library()
    while True:
        print("\nLibrary Manager")
        print("1. List books")
        print("2. Add book")
        print("3. Mark read/unread")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            mark_read(books)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
