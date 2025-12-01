def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def main():
    text = input("Temperature in °C: ")
    try:
        c = float(text)
    except ValueError:
        print("Please enter a number.")
        return
    f = c_to_f(c)
    print(f"{c:.1f}°C is {f:.1f}°F")

if __name__ == "__main__":
    main()
