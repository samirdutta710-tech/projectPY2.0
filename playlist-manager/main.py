import json
import os
import random
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "playlist.json"

@dataclass
class Track:
    title: str
    artist: str
    rating: int  # 1-5

def load_tracks() -> List[Track]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Track(**t) for t in data]

def save_tracks(tracks: List[Track]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in tracks], f, indent=2)

def add_track(tracks: List[Track]):
    title = input("Title: ").strip()
    artist = input("Artist: ").strip()
    try:
        rating = int(input("Rating (1-5): "))
    except ValueError:
        print("Rating must be number 1-5.")
        return
    if rating < 1 or rating > 5:
        print("Rating must be 1-5.")
        return
    tracks.append(Track(title=title, artist=artist, rating=rating))
    save_tracks(tracks)
    print("Added.")

def list_tracks(tracks: List[Track]):
    if not tracks:
        print("No tracks.")
        return
    for i, t in enumerate(tracks, start=1):
        print(f"{i}. {t.title} - {t.artist} ({t.rating}/5)")

def shuffle_tracks(tracks: List[Track]):
    random.shuffle(tracks)
    list_tracks(tracks)

def sort_by_rating(tracks: List[Track]):
    tracks.sort(key=lambda t: t.rating, reverse=True)
    list_tracks(tracks)

def main():
    tracks = load_tracks()
    while True:
        print("\nPlaylist Manager")
        print("1. List tracks")
        print("2. Add track")
        print("3. Shuffle")
        print("4. Sort by rating")
        print("5. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_tracks(tracks)
        elif choice == "2":
            add_track(tracks)
        elif choice == "3":
            shuffle_tracks(tracks)
            save_tracks(tracks)
        elif choice == "4":
            sort_by_rating(tracks)
            save_tracks(tracks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
