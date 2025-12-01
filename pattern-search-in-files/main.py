from pathlib import Path

def search_in_file(path: Path, pattern: str):
    matches = []
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return matches
    for i, line in enumerate(lines, start=1):
        if pattern.lower() in line.lower():
            matches.append((i, line))
    return matches

def main():
    folder = input("Folder to search (default .): ").strip() or "."
    pattern = input("Text to search for: ").strip()
    if not pattern:
        print("Pattern required.")
        return

    base = Path(folder)
    if not base.is_dir():
        print("Not a directory.")
        return

    any_match = False
    for path in base.rglob("*.txt"):
        results = search_in_file(path, pattern)
        if results:
            any_match = True
            print(f"\nFile: {path}")
            for lineno, line in results:
                print(f"  {lineno}: {line}")
    if not any_match:
        print("No matches found.")

if __name__ == "__main__":
    main()
