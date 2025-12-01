import requests
from pathlib import Path

def load_urls(path: str):
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"No such file: {p}")
    return [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

def check_url(url: str, timeout: float = 5.0):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code
    except requests.RequestException as e:
        return f"ERROR: {e.__class__.__name__}"

def main():
    path = input("Path to file containing URLs (one per line): ").strip()
    try:
        urls = load_urls(path)
    except Exception as e:
        print("Error:", e)
        return

    print("\nChecking URLs...")
    for url in urls:
        status = check_url(url)
        print(f"{url} -> {status}")

if __name__ == "__main__":
    main()
