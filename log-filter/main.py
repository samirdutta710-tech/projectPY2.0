from pathlib import Path
from collections import Counter

LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def read_log(path: str):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"No such file: {p}")
    return p.read_text(encoding="utf-8").splitlines()

def summarize_levels(lines):
    counter = Counter()
    for line in lines:
        for level in LEVELS:
            if f"{level}" in line:
                counter[level] += 1
                break
    return counter

def filter_by_level(lines, level):
    return [line for line in lines if level in line]

def main():
    log_path = input("Path to log file: ").strip()
    try:
        lines = read_log(log_path)
    except Exception as e:
        print("Error:", e)
        return

    counts = summarize_levels(lines)
    print("\nLog level summary:")
    for level in LEVELS:
        if counts[level]:
            print(f"{level}: {counts[level]}")

    level = input("\nEnter level to filter (e.g. ERROR) or leave blank to quit: ").upper().strip()
    if level and level in LEVELS:
        filtered = filter_by_level(lines, level)
        print(f"\nLines containing {level}:")
        for line in filtered:
            print(line)
    elif level:
        print("Unknown level.")

if __name__ == "__main__":
    main()
