def main():
    print("Enter names (empty line to stop):")
    names = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        names.append(name)

    if not names:
        print("No names entered.")
        return

    print("\nGreetings:")
    for name in names:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
