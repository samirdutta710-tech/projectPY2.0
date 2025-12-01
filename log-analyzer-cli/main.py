from pathlib import Path
from collections import defaultdict

def parse_log_line(line: str):
    # Expected format: [DATE TIME] [LEVEL] message...
    try:
        if not line.startswith("["):
            return None
        date_end = line.index("]")
        datetime_str = line[1:date_end]  # "2025-12-01 10:00:00"
        rest = line[date_end+2:]
        if not rest.startswith("["):
            return None
        level_end = rest.index("]")
        level = rest[1:level_end].upper()
        message = rest[level_end+2:].strip()
        day = datetime_str.split(" ")[0]  # "2025-12-01"
        return day, level, message
    except (ValueError, IndexError):
        return None

def load_log(path: str):
    p = Path(path)
    if not p.is_file():
        print("File not found.")
        return []
    lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
    parsed = []
    for line in lines:
        info = parse_log_line(line)
        if info:
            parsed.append(info)
    return parsed

def show_summary(entries):
    if not entries:
        print("No valid log entries.")
        return
    by_level = defaultdict(int)
    by_day = defaultdict(int)
    for day, level, _ in entries:
        by_level[level] += 1
        by_day[day] += 1

    print("\nLog entries per level:")
    for level, count in sorted(by_level.items()):
        print(f"- {level}: {count}")

    print("\nLog entries per day:")
    for day, count in sorted(by_day.items()):
        print(f"- {day}: {count}")

def filter_by_level(entries, level):
    level = level.upper()
    return [e for e in entries if e[1] == level]

def main():
    path = input("Path to log file: ").strip()
    entries = load_log(path)
    if not entries:
        return

    while True:
        print("\nLog Analyzer CLI")
        print("1. Show summary")
        print("2. Show entries for a level (e.g. ERROR)")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            show_summary(entries)
        elif choice == "2":
            lvl = input("Level: ").strip()
            subset = filter_by_level(entries, lvl)
            if not subset:
                print("No entries for that level.")
            else:
                for day, level, msg in subset:
                    print(f"[{day}] [{level}] {msg}")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
