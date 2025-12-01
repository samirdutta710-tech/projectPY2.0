from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"  # e.g. 2025-12-01

def read_date(prompt: str):
    text = input(prompt).strip()
    try:
        return datetime.strptime(text, DATE_FORMAT).date()
    except ValueError:
        print(f"Date must be in format {DATE_FORMAT}.")
        return None

def main():
    print("📆 Day Counter")
    d1 = read_date("Enter first date (YYYY-MM-DD): ")
    if not d1:
        return
    d2 = read_date("Enter second date (YYYY-MM-DD): ")
    if not d2:
        return

    diff = (d2 - d1).days
    print(f"\nDifference: {diff} days")

if __name__ == "__main__":
    main()
