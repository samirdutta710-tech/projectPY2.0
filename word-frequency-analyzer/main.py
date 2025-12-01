from collections import Counter
import re
from pathlib import Path

def load_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"No such file: {file_path}")
    return file_path.read_text(encoding="utf-8")

def count_words(text: str):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return Counter(words)

def main():
    filename = input("Enter path to a .txt file: ").strip()
    try:
        text = load_text(filename)
    except Exception as e:
        print("Error:", e)
        return

    counts = count_words(text)
    top_n_str = input("How many top words to show? (default 10): ").strip()
    top_n = int(top_n_str) if top_n_str.isdigit() else 10

    print(f"\nTop {top_n} words:")
    for word, freq in counts.most_common(top_n):
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
