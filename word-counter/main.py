def analyze_text(text: str):
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    return len(lines), len(words), chars

def main():
    print("🔢 Word Counter")
    print("Type/paste your text. End with an empty line.")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    num_lines, num_words, num_chars = analyze_text(text)

    print("\nResults:")
    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")

if __name__ == "__main__":
    main()
