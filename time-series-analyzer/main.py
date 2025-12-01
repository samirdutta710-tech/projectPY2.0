import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List

DATE_FMT = "%Y-%m-%d %H:%M:%S"  # example: 2025-12-01 14:30:00

def load_data(path: str):
    p = Path(path)
    if not p.is_file():
        print("File not found.")
        return []
    rows = []
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) != 2:
                continue
            ts_str, val_str = row
            try:
                ts = datetime.strptime(ts_str, DATE_FMT)
                val = float(val_str)
            except ValueError:
                continue
            rows.append((ts, val))
    return rows

def summarize(rows):
    per_day: Dict[str, List[float]] = {}
    for ts, val in rows:
        key = ts.date().isoformat()
        per_day.setdefault(key, []).append(val)

    print("\nDaily summary:")
    for day in sorted(per_day.keys()):
        vals = per_day[day]
        total = sum(vals)
        avg = total / len(vals)
        print(f"{day} -> count={len(vals)}, total={total:.2f}, avg={avg:.2f}")

def main():
    path = input("CSV file path: ").strip()
    rows = load_data(path)
    if not rows:
        print("No valid rows.")
        return
    summarize(rows)

if __name__ == "__main__":
    main()
