def main():
    print("💸 Tip Splitter")

    try:
        bill = float(input("Bill amount: "))
        tip_percent = float(input("Tip percent (e.g. 15): "))
        people = int(input("How many people? "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if people <= 0:
        print("Number of people must be at least 1.")
        return

    tip_amount = bill * tip_percent / 100
    total = bill + tip_amount
    per_person = total / people

    print(f"\nBill: ${bill:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Each person pays: ${per_person:.2f}")

if __name__ == "__main__":
    main()
