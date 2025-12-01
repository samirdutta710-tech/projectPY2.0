import string
import random

def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.?/")

    if not chars:
        raise ValueError("No character sets selected.")

    return "".join(random.choice(chars) for _ in range(length))

def yes_no(prompt: str) -> bool:
    ans = input(prompt + " (y/n): ").strip().lower()
    return ans == "y"

def main():
    print("🔑 Random Password Generator")
    length_str = input("Password length (e.g. 12): ").strip()
    if not length_str.isdigit():
        print("Length must be a positive integer.")
        return
    length = int(length_str)
    if length <= 0:
        print("Length must be positive.")
        return

    use_upper = yes_no("Include uppercase letters?")
    use_digits = yes_no("Include digits?")
    use_symbols = yes_no("Include symbols?")

    try:
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
    except ValueError as e:
        print("Error:", e)
        return

    print("\nGenerated password:")
    print(pwd)

if __name__ == "__main__":
    main()
