def km_to_miles(km: float) -> float:
    return km * 0.621371

def miles_to_km(miles: float) -> float:
    return miles / 0.621371

def kg_to_lb(kg: float) -> float:
    return kg * 2.20462

def lb_to_kg(lb: float) -> float:
    return lb / 2.20462

def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9

def read_float(prompt: str):
    text = input(prompt)
    try:
        return float(text)
    except ValueError:
        print("Invalid number.")
        return None

def main():
    while True:
        print("\nUnit Converter CLI")
        print("1. Kilometers -> Miles")
        print("2. Miles -> Kilometers")
        print("3. Kilograms -> Pounds")
        print("4. Pounds -> Kilograms")
        print("5. Celsius -> Fahrenheit")
        print("6. Fahrenheit -> Celsius")
        print("7. Quit")
        choice = input("Choose: ")

        if choice == "1":
            v = read_float("Kilometers: ")
            if v is not None:
                print(f"{v} km = {km_to_miles(v):.2f} mi")
        elif choice == "2":
            v = read_float("Miles: ")
            if v is not None:
                print(f"{v} mi = {miles_to_km(v):.2f} km")
        elif choice == "3":
            v = read_float("Kilograms: ")
            if v is not None:
                print(f"{v} kg = {kg_to_lb(v):.2f} lb")
        elif choice == "4":
            v = read_float("Pounds: ")
            if v is not None:
                print(f"{v} lb = {lb_to_kg(v):.2f} kg")
        elif choice == "5":
            v = read_float("Celsius: ")
            if v is not None:
                print(f"{v} °C = {c_to_f(v):.2f} °F")
        elif choice == "6":
            v = read_float("Fahrenheit: ")
            if v is not None:
                print(f"{v} °F = {f_to_c(v):.2f} °C")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
