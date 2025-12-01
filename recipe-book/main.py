import json
import os
from dataclasses import dataclass, asdict
from typing import List

FILE_NAME = "recipes.json"

@dataclass
class Recipe:
    name: str
    ingredients: List[str]
    steps: List[str]

def load_recipes() -> List[Recipe]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Recipe(**r) for r in data]

def save_recipes(recipes: List[Recipe]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in recipes], f, indent=2)

def list_recipes(recipes: List[Recipe]):
    if not recipes:
        print("No recipes yet.")
        return
    for i, r in enumerate(recipes, start=1):
        print(f"{i}. {r.name}")

def view_recipe(recipes: List[Recipe]):
    list_recipes(recipes)
    idx_str = input("Recipe number to view: ").strip()
    if not idx_str.isdigit():
        print("Invalid number.")
        return
    idx = int(idx_str) - 1
    if not (0 <= idx < len(recipes)):
        print("Out of range.")
        return
    r = recipes[idx]
    print(f"\n== {r.name} ==")
    print("\nIngredients:")
    for ing in r.ingredients:
        print(f"- {ing}")
    print("\nSteps:")
    for i, step in enumerate(r.steps, start=1):
        print(f"{i}. {step}")

def add_recipe(recipes: List[Recipe]):
    name = input("Recipe name: ").strip()
    if not name:
        print("Name required.")
        return

    print("Enter ingredients (empty line to stop):")
    ingredients = []
    while True:
        line = input("> ").strip()
        if not line:
            break
        ingredients.append(line)

    print("Enter steps (empty line to stop):")
    steps = []
    while True:
        line = input("> ").strip()
        if not line:
            break
        steps.append(line)

    recipes.append(Recipe(name=name, ingredients=ingredients, steps=steps))
    save_recipes(recipes)
    print("Recipe added.")

def main():
    recipes = load_recipes()
    while True:
        print("\nRecipe Book")
        print("1. List recipes")
        print("2. View recipe")
        print("3. Add recipe")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_recipes(recipes)
        elif choice == "2":
            view_recipe(recipes)
        elif choice == "3":
            add_recipe(recipes)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
