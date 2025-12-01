from pathlib import Path

def extract_headings(path: Path):
    headings = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.lstrip()
        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            title = stripped[level:].strip()
            headings.append((level, title))
    return headings

def build_index(root: str, output: str = "index.txt"):
    base = Path(root)
    if not base.is_dir():
        print("Not a directory.")
        return
    lines = []
    for md in sorted(base.rglob("*.md")):
        rel = md.relative_to(base)
        lines.append(f"\nFile: {rel}")
        for level, title in extract_headings(md):
            indent = "  " * (level - 1)
            lines.append(f"{indent}- {title}")
    Path(output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Index written to {output}")

def main():
    folder = input("Folder with markdown files (default .): ").strip() or "."
    build_index(folder)

if __name__ == "__main__":
    main()
