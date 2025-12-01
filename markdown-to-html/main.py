from pathlib import Path

def convert_line(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith("### "):
        return f"<h3>{stripped[4:]}</h3>"
    if stripped.startswith("## "):
        return f"<h2>{stripped[3:]}</h2>"
    if stripped.startswith("# "):
        return f"<h1>{stripped[2:]}</h1>"
    if stripped == "":
        return "<br>"
    return f"<p>{stripped}</p>"

def convert_markdown(md_path: str, html_path: str) -> None:
    src = Path(md_path)
    if not src.is_file():
        raise FileNotFoundError(f"No such file: {src}")
    lines = src.read_text(encoding="utf-8").splitlines()
    converted = [convert_line(line) for line in lines]
    html = "<html><body>\n" + "\n".join(converted) + "\n</body></html>"
    Path(html_path).write_text(html, encoding="utf-8")

def main():
    src = input("Markdown file path: ").strip()
    dst = input("Output HTML file path (default: output.html): ").strip() or "output.html"
    try:
        convert_markdown(src, dst)
        print(f"Converted and saved to {dst}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
