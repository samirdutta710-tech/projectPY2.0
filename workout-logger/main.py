import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "workouts.json"

@dataclass
class Workout:
    exercise: str
    sets: int
    reps: int
    weight: float  # per rep

def load_workouts() -> List[Workout]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Workout(**w) for w in data]

def save_workouts(workouts: List[Workout]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(w) for w in workouts], f, indent=2)

def add_workout(workouts: List[Workout]):
    exercise = input("Exercise name: ").strip()
    sets_str = input("Sets: ").strip()
    reps_str = input("Reps per set: ").strip()
    weight_str = input("Weight per rep (kg): ").strip()
    try:
        sets = int(sets_str)
        reps = int(reps_str)
        weight = float(weight_str)
    except ValueError:
        print("Invalid number.")
        return
    workouts.append(Workout(exercise=exercise, sets=sets, reps=reps, weight=weight))
    save_workouts(workouts)
    print("Workout logged.")

def show_summary(workouts: List[Workout]):
    if not workouts:
        print("No workouts yet.")
        return
    totals = {}
    for w in workouts:
        volume = w.sets * w.reps * w.weight
        totals[w.exercise] = totals.get(w.exercise, 0) + volume
    print("\nTotal volume (sets * reps * weight) per exercise:")
    for ex, vol in totals.items():
        print(f"- {ex}: {vol:.1f} kg")

def main():
    workouts = load_workouts()
    while True:
        print("\nWorkout Logger")
        print("1. Add workout")
        print("2. Show volume summary")
        print("3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_workout(workouts)
        elif choice == "2":
            show_summary(workouts)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
