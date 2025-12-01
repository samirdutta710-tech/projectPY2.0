import shutil
from pathlib import Path
from datetime import datetime

def backup_directory(src_path: str):
    src = Path(src_path)
    if not src.is_dir():
        raise NotADirectoryError(f"{src} is not a directory")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = src.parent / f"{src.name}_backup_{timestamp}"
    shutil.copytree(src, dest)
    return dest

def main():
    folder = input("Folder to back up (default = current directory): ").strip()
    if not folder:
        folder = "."

    try:
        dest = backup_directory(folder)
        print(f"Backup created at: {dest}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
