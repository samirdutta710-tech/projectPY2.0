import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".gif": "images",
    ".pdf": "documents",
    ".txt": "documents",
    ".docx": "documents",
    ".mp3": "audio",
    ".wav": "audio",
}

def organize(folder):
    folder = Path(folder)
    if not folder.is_dir():
        print("Not a valid folder.")
        return

    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            target_dir_name = EXTENSION_MAP.get(ext, "others")
            target_dir = folder / target_dir_name
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
    print("Organization complete.")

def main():
    path = input("Enter folder path to organize (or leave blank for current): ").strip()
    if not path:
        path = "."
    organize(path)

if __name__ == "__main__":
    main()
