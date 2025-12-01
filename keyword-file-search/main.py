from pathlib import Path

def search_in_file(path: Path, keyword: str) -> list[str]:
    matches = []
    try:
        with path.open("r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if keyword.lower() in line.lower():
                    matches.append(f"{path} (line {i}): {line.strip()}")
    except UnicodeDecodeError:
        # Skip non-text files
        pass
    return matches

def search_directory(root: str, keyword: str) -> None:
    base = Path(root)
    if not base.is_dir():
        print("Not a directory.")
        return
    total_matches = 0
    for path in base.rglob("*.txt"):
        matches = search_in_file(path, keyword)
        for m in matches:
            print(m)
        total_matches += len(matches)
    print(f"Found {total_matches} matches.")

def main():
    root = input("Directory to search (default .): ").strip() or "."
    keyword = input("Keyword to search for: ").strip()
    if not keyword:
        print("Keyword required.")
        return
    search_directory(root, keyword)

if __name__ == "__main__":
    main()
