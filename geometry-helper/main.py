import math

def rectangle():
    try:
        w = float(input("Width: "))
        h = float(input("Height: "))
    except ValueError:
        print("Invalid number.")
        return
    area = w * h
    perimeter = 2 * (w + h)
    print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")

def circle():
    try:
        r = float(input("Radius: "))
    except ValueError:
        print("Invalid number.")
        return
    if r < 0:
        print("Radius cannot be negative.")
        return
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")

def main():
    while True:
        print("\nGeometry Helper")
        print("1. Rectangle (area & perimeter)")
        print("2. Circle (area & circumference)")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            rectangle()
        elif choice == "2":
            circle()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
