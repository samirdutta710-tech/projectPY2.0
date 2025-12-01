import random

def roll_dice(num_dice: int, sides: int):
    return [random.randint(1, sides) for _ in range(num_dice)]

def main():
    print("🎲 Dice Roller")

    while True:
        num = input("How many dice? (or 'q' to quit): ").strip()
        if num.lower() == "q":
            break
        sides = input("How many sides per die? ").strip()

        if not (num.isdigit() and sides.isdigit()):
            print("Please enter positive whole numbers.")
            continue

        num_dice = int(num)
        num_sides = int(sides)

        rolls = roll_dice(num_dice, num_sides)
        print("Rolls:", rolls)
        print("Total:", sum(rolls))

if __name__ == "__main__":
    main()
