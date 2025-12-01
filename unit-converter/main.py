def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def main():
    while True:
        print("\nUnit Converter")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")
        print("3. Meters -> Feet")
        print("4. Feet -> Meters")
        print("5. Kilograms -> Pounds")
        print("6. Pounds -> Kilograms")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "7":
            print("Goodbye!")
            break

        value = input("Enter value: ")
        try:
            value = float(value)
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == "1":
            print(c_to_f(value))
        elif choice == "2":
            print(f_to_c(value))
        elif choice == "3":
            print(meters_to_feet(value))
        elif choice == "4":
            print(feet_to_meters(value))
        elif choice == "5":
            print(kg_to_lb(value))
        elif choice == "6":
            print(lb_to_kg(value))
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
