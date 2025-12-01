import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = "!@#$%^&*()-_=+[]" if use_symbols else ""

    all_chars = letters + digits + symbols
    if not all_chars:
        raise ValueError("No characters available to generate password.")

    return "".join(random.choice(all_chars) for _ in range(length))

def main():
    print("🔐 Password Generator")

    length = input("Password length (default 12): ").strip()
    length = int(length) if length.isdigit() else 12

    use_digits = input("Include digits? (y/n, default y): ").strip().lower() != "n"
    use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != "n"

    pwd = generate_password(length, use_digits, use_symbols)
    print(f"Generated password: {pwd}")

if __name__ == "__main__":
    main()
