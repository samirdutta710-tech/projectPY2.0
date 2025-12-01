import string

def check_strength(password: str) -> str:
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    if length < 6 or score <= 1:
        return "Very weak"
    elif length < 8:
        return "Weak"
    elif score == 2:
        return "Medium"
    elif score == 3:
        return "Strong"
    else:
        return "Very strong"

def main():
    print("🔐 Password Strength Checker")
    pwd = input("Enter a password to check: ")
    strength = check_strength(pwd)
    print(f"Strength: {strength}")

if __name__ == "__main__":
    main()
