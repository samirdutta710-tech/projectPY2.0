import random
from pathlib import Path

def load_names(path: str) -> list[str]:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"No such file: {p}")
    return [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]

def make_teams(names: list[str], team_size: int) -> list[list[str]]:
    random.shuffle(names)
    return [names[i:i+team_size] for i in range(0, len(names), team_size)]

def main():
    path = input("Path to file with one name per line: ").strip()
    try:
        names = load_names(path)
    except Exception as e:
        print("Error:", e)
        return
    if not names:
        print("No names found.")
        return
    size_str = input("Team size (e.g. 3): ").strip()
    if not size_str.isdigit() or int(size_str) <= 0:
        print("Invalid team size.")
        return
    team_size = int(size_str)
    teams = make_teams(names, team_size)
    for i, team in enumerate(teams, start=1):
        print(f"Team {i}: {', '.join(team)}")

if __name__ == "__main__":
    main()
