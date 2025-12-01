import csv
from pathlib import Path

def load_csv(path: str):
    p = Path(path)
    if not p.is_file():
        print("File not found.")
        return [], []
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return [], []
    header = rows[0]
    data = rows[1:]
    return header, data

def choose_columns(header):
    print("\nAvailable columns:")
    for i, col in enumerate(header, start=1):
        print(f"{i}. {col}")
    cols_str = input("Columns to show (comma separated numbers, empty = all): ").strip()
    if not cols_str:
        return list(range(len(header)))
    idxs = []
    for part in cols_str.split(","):
        part = part.strip()
        if part.isdigit():
            idx = int(part) - 1
            if 0 <= idx < len(header):
                idxs.append(idx)
    return idxs or list(range(len(header)))

def choose_sort_column(header):
    print("\nSort by which column? (or empty for no sorting)")
    for i, col in enumerate(header, start=1):
        print(f"{i}. {col}")
    s = input("Column number: ").strip()
    if not s:
        return None
    if not s.isdigit():
        return None
    idx = int(s) - 1
    if 0 <= idx < len(header):
        return idx
    return None

def main():
    path = input("CSV file path: ").strip()
    header, data = load_csv(path)
    if not header:
        print("No data.")
        return

    col_idxs = choose_columns(header)
    sort_idx = choose_sort_column(header)

    if sort_idx is not None:
        data.sort(key=lambda row: row[sort_idx])

    print("\nSelected data:\n")
    selected_header = [header[i] for i in col_idxs]
    print(" | ".join(selected_header))
    print("-" * (len(" | ".join(selected_header)) + 3))

    for row in data:
        selected_row = [row[i] for i in col_idxs]
        print(" | ".join(selected_row))

if __name__ == "__main__":
    main()
