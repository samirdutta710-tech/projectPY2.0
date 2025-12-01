import math

def main():
    r_str = input("Radius: ")
    try:
        r = float(r_str)
    except ValueError:
        print("Please enter a number.")
        return
    if r < 0:
        print("Radius cannot be negative.")
        return
    area = math.pi * r * r
    print(f"Area: {area:.2f}")

if __name__ == "__main__":
    main()
