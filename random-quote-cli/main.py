import random

QUOTES = [
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "In order to be irreplaceable, one must always be different.",
    "Java is to JavaScript what car is to carpet.",
]

def main():
    print("🎯 Random Quote CLI")
    while True:
        cmd = input("Press Enter for a quote, or 'q' to quit: ").strip().lower()
        if cmd == "q":
            break
        quote = random.choice(QUOTES)
        print("\n" + quote + "\n")

if __name__ == "__main__":
    main()
