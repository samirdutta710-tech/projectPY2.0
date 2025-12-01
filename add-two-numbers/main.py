def main():
    a = input("First number: ")
    b = input("Second number: ")

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("Sum:", a + b)

if __name__ == "__main__":
    main()
