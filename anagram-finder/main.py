from pathlib import Path
from collections import defaultdict

def load_dictionary(path: str):
    p = Path(path)
    if not p.is_file():
        print("Dictionary file not found.")
        return {}
    anagram_map = defaultdict(list)
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        word = line.strip()
        if not word:
            continue
        key = "".join(sorted(word.lower()))
        anagram_map[key].append(word)
    return anagram_map

def find_anagrams(anagram_map, word: str):
    key = "".join(sorted(word.lower()))
    words = anagram_map.get(key, [])
    # Exclude the word itself (case-insensitive)
    return [w for w in words if w.lower() != word.lower()]

def main():
    dict_path = input("Dictionary file path (one word per line): ").strip()
    anagram_map = load_dictionary(dict_path)
    if not anagram_map:
        return

    while True:
        word = input("\nEnter a word (or 'q' to quit): ").strip()
        if word.lower() == "q":
            break
        anagrams = find_anagrams(anagram_map, word)
        if anagrams:
            print("Anagrams found:")
            for w in anagrams:
                print("-", w)
        else:
            print("No anagrams found (in this dictionary).")

if __name__ == "__main__":
    main()
