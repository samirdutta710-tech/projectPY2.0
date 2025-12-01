import string

ALPHABET = string.ascii_lowercase

def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.lower() in ALPHABET:
            idx = ALPHABET.index(ch.lower())
            new_idx = (idx + shift) % 26
            new_char = ALPHABET[new_idx]
            if ch.isupper():
                new_char = new_char.upper()
            result.append(new_char)
        else:
            result.append(ch)
    return "".join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Tool")
    mode = input("Mode (e)ncrypt or (d)ecrypt: ").strip().lower()
    if mode not in {"e", "d"}:
        print("Invalid mode.")
        return
    try:
        shift = int(input("Shift (e.g. 3): "))
    except ValueError:
        print("Shift must be an integer.")
        return
    text = input("Enter text: ")
    if mode == "e":
        print("Encrypted:", caesar_encrypt(text, shift))
    else:
        print("Decrypted:", caesar_decrypt(text, shift))

if __name__ == "__main__":
    main()
