import calendar

def main():
    print("📅 Simple Calendar Viewer")
    year_str = input("Year (e.g. 2025): ").strip()
    month_str = input("Month (1-12): ").strip()

    if not (year_str.isdigit() and month_str.isdigit()):
        print("Please enter valid numbers.")
        return

    year = int(year_str)
    month = int(month_str)

    if not (1 <= month <= 12):
        print("Month must be between 1 and 12.")
        return

    print()
    print(calendar.month(year, month))

if __name__ == "__main__":
    main()
