from pathlib import Path

def scan_dir(root: Path) -> dict[str, int]:
    files = {}
    for p in root.rglob("*"):
        if p.is_file():
            rel = str(p.relative_to(root))
            files[rel] = p.stat().st_size
    return files

def main():
    src = Path(input("Source folder: ").strip() or ".")
    dst = Path(input("Destination folder: ").strip() or ".")

    if not src.is_dir() or not dst.is_dir():
        print("Both must be directories.")
        return

    src_files = scan_dir(src)
    dst_files = scan_dir(dst)

    missing = [f for f in src_files if f not in dst_files]
    extra = [f for f in dst_files if f not in src_files]
    different = [f for f in src_files if f in dst_files and src_files[f] != dst_files[f]]

    print("\nMissing in destination:")
    for f in missing:
        print("-", f)

    print("\nExtra in destination:")
    for f in extra:
        print("-", f)

    print("\nDifferent size:")
    for f in different:
        print(f"- {f}: src={src_files[f]} bytes, dst={dst_files[f]} bytes")

if __name__ == "__main__":
    main()
