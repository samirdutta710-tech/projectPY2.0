from pathlib import Path
import shutil

def organize(path_str: str):
    base = Path(path_str)
    if not base.is_dir():
        print("Not a directory.")
        return

    for item in base.iterdir():
        if item.is_file():
            ext = item.suffix.lower().lstrip(".") or "no_extension"
            target_dir = base / ext
            target_dir.mkdir(exist_ok=True)
            new_path = target_dir / item.name
            print(f"Moving {item.name} -> {target_dir}/")
            shutil.move(str(item), str(new_path))

def main():
    folder = input("Folder to organize (default .): ").strip() or "."
    organize(folder)
    print("Done organizing.")

if __name__ == "__main__":
    main()
