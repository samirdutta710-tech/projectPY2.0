from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import urllib.parse

POSTS_DIR = Path("posts")

def markdown_to_html(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            lines.append(f"<h1>{stripped[2:]}</h1>")
        elif stripped.startswith("## "):
            lines.append(f"<h2>{stripped[3:]}</h2>")
        else:
            lines.append(f"<p>{stripped}</p>")
    return "\n".join(lines)

def list_posts() -> str:
    POSTS_DIR.mkdir(exist_ok=True)
    items = []
    for p in POSTS_DIR.glob("*.md"):
        name = p.stem
        items.append(f'<li><a href="/post/{name}">{name}</a></li>')
    return "<ul>" + "".join(items) + "</ul>"

class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path == "/":
            content = "<h1>Mini Blog</h1>" + list_posts()
        elif path.startswith("/post/"):
            slug = path[len("/post/"):]
            md_path = POSTS_DIR / f"{slug}.md"
            if not md_path.is_file():
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Not found")
                return
            html_body = markdown_to_html(md_path.read_text(encoding="utf-8"))
            content = f"<h1>{slug}</h1>" + html_body
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")
            return

        html = f"<!doctype html><html><body>{content}</body></html>"
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

def main():
    POSTS_DIR.mkdir(exist_ok=True)
    server = HTTPServer(("localhost", 8000), BlogHandler)
    print("Mini blog running at http://localhost:8000")
    server.serve_forever()

if __name__ == "__main__":
    main()
