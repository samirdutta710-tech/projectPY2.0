import csv
from pathlib import Path
from statistics import mean

def load_grades(path: str):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"No such file: {p}")
    students = []
    with p.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            name = row[0]
            try:
                grades = [float(x) for x in row[1:] if x.strip() != ""]
            except ValueError:
                print(f"Skipping row with invalid grade: {row}")
                continue
            students.append((name, grades))
    return students

def main():
    path = input("Path to grades CSV: ").strip()
    try:
        students = load_grades(path)
    except Exception as e:
        print("Error:", e)
        return

    if not students:
        print("No valid data.")
        return

    from statistics import mean
    print("\nStudent averages:")
    all_grades = []
    for name, grades in students:
        avg = mean(grades)
        all_grades.extend(grades)
        print(f"{name}: {avg:.2f}")

    print(f"\nClass average: {mean(all_grades):.2f}")
    print(f"Highest grade: {max(all_grades):.2f}")
    print(f"Lowest grade: {min(all_grades):.2f}")

if __name__ == "__main__":
    main()
