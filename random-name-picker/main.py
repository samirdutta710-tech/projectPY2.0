import random

def main():
    print("🎟️ Random Name Picker")
    names = []

    print("Enter names one per line. Leave empty line to finish.")
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        names.append(name)

    if not names:
        print("No names entered.")
        return

    while True:
        cmd = input("\nType 'pick' to choose a random name, or 'q' to quit: ").strip().lower()
        if cmd == "q":
            break
        if cmd == "pick":
            chosen = random.choice(names)
            print(f"Chosen: {chosen}")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
