import string

def clean_text(text: str) -> str:
    allowed = string.ascii_letters + string.digits
    return "".join(ch.lower() for ch in text if ch in allowed)

def is_palindrome(text: str) -> bool:
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]

def main():
    print("🔁 Palindrome Checker")
    while True:
        text = input("\nEnter text (or 'q' to quit): ")
        if text.lower() == "q":
            break
        if is_palindrome(text):
            print("Yes, that's a palindrome!")
        else:
            print("Nope, not a palindrome.")

if __name__ == "__main__":
    main()
