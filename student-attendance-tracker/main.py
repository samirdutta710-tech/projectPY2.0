import json
import os
from dataclasses import dataclass, asdict
from datetime import date

FILE_NAME = "attendance.json"

@dataclass
class AttendanceData:
    students: list[str]
    records: dict  # date -> list of present student names

def load_data() -> AttendanceData:
    if not os.path.exists(FILE_NAME):
        return AttendanceData(students=[], records={})
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return AttendanceData(students=data["students"], records=data["records"])

def save_data(data: AttendanceData) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump({"students": data.students, "records": data.records}, f, indent=2)

def add_student(data: AttendanceData) -> None:
    name = input("Student name: ").strip()
    if not name:
        print("Name required.")
        return
    if name in data.students:
        print("Already exists.")
        return
    data.students.append(name)
    save_data(data)
    print("Student added.")

def list_students(data: AttendanceData) -> None:
    if not data.students:
        print("No students.")
        return
    for i, s in enumerate(data.students, start=1):
        print(f"{i}. {s}")

def take_attendance(data: AttendanceData) -> None:
    if not data.students:
        print("No students to mark.")
        return
    today = date.today().isoformat()
    present = []
    print("Mark attendance (y/n):")
    for s in data.students:
        ans = input(f"{s}: ").strip().lower()
        if ans == "y":
            present.append(s)
    data.records[today] = present
    save_data(data)
    print("Attendance saved.")

def show_record(data: AttendanceData) -> None:
    if not data.records:
        print("No records yet.")
        return
    for d, present in sorted(data.records.items()):
        print(f"{d}: {len(present)} present -> {', '.join(present)}")

def main():
    data = load_data()
    while True:
        print("\nAttendance Tracker")
        print("1. List students")
        print("2. Add student")
        print("3. Take attendance for today")
        print("4. Show records")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_students(data)
        elif choice == "2":
            add_student(data)
        elif choice == "3":
            take_attendance(data)
        elif choice == "4":
            show_record(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
