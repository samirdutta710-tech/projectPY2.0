import json
import os
from dataclasses import dataclass, asdict
from typing import Dict, List

FILE_NAME = "gradebook.json"

@dataclass
class Gradebook:
    students: Dict[str, Dict[str, float]]  # student -> {assignment: grade}

def load_gradebook() -> Gradebook:
    if not os.path.exists(FILE_NAME):
        return Gradebook(students={})
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return Gradebook(students=data.get("students", {}))

def save_gradebook(gb: Gradebook):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump({"students": gb.students}, f, indent=2)

def add_student(gb: Gradebook):
    name = input("Student name: ").strip()
    if not name:
        print("Name required.")
        return
    if name in gb.students:
        print("Student already exists.")
        return
    gb.students[name] = {}
    save_gradebook(gb)
    print("Student added.")

def add_grade(gb: Gradebook):
    name = input("Student name: ").strip()
    if name not in gb.students:
        print("No such student.")
        return
    assignment = input("Assignment name: ").strip()
    try:
        grade = float(input("Grade (0-100): "))
    except ValueError:
        print("Invalid grade.")
        return
    gb.students[name][assignment] = grade
    save_gradebook(gb)
    print("Grade recorded.")

def show_student(gb: Gradebook):
    name = input("Student name: ").strip()
    if name not in gb.students:
        print("No such student.")
        return
    grades = gb.students[name]
    if not grades:
        print("No grades yet.")
        return
    total = sum(grades.values())
    avg = total / len(grades)
    print(f"\n{name}'s grades:")
    for a, g in grades.items():
        print(f"- {a}: {g}")
    print(f"Average: {avg:.2f}")

def show_class_averages(gb: Gradebook):
    if not gb.students:
        print("No students.")
        return
    assignment_totals: Dict[str, List[float]] = {}
    for grades in gb.students.values():
        for a, g in grades.items():
            assignment_totals.setdefault(a, []).append(g)
    if not assignment_totals:
        print("No grades recorded.")
        return
    print("\nClass averages per assignment:")
    for a, lst in assignment_totals.items():
        avg = sum(lst) / len(lst)
        print(f"- {a}: {avg:.2f}")

def main():
    gb = load_gradebook()
    while True:
        print("\nGradebook Manager")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show student grades")
        print("4. Show class assignment averages")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_student(gb)
        elif choice == "2":
            add_grade(gb)
        elif choice == "3":
            show_student(gb)
        elif choice == "4":
            show_class_averages(gb)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
