import json
import os
from dataclasses import dataclass, asdict
from typing import List, Dict

FILE_NAME = "recipes.json"

@dataclass
class Recipe:
    name: str
    ingredients: List[str]  # e.g. "2 eggs", "200g flour"

def load_recipes() -> List[Recipe]:
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Recipe(**r) for r in data]

def save_recipes(recipes: List[Recipe]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in recipes], f, indent=2)

def add_recipe(recipes: List[Recipe]):
    name = input("Recipe name: ").strip()
    if not name:
        print("Name required.")
        return
    print("Enter ingredients (empty line to finish):")
    ings = []
    while True:
        line = input("> ").strip()
        if not line:
            break
        ings.append(line)
    recipes.append(Recipe(name=name, ingredients=ings))
    save_recipes(recipes)
    print("Recipe added.")

def list_recipes(recipes: List[Recipe]):
    if not recipes:
        print("No recipes.")
        return
    for i, r in enumerate(recipes, start=1):
        print(f"{i}. {r.name}")

def plan_meals(recipes: List[Recipe]):
    if not recipes:
        print("No recipes.")
        return
    list_recipes(recipes)
    print("Enter recipe numbers to cook (comma separated):")
    nums = input("> ").split(",")
    chosen: List[Recipe] = []
    for n in nums:
        n = n.strip()
        if not n.isdigit():
            continue
        idx = int(n) - 1
        if 0 <= idx < len(recipes):
            chosen.append(recipes[idx])
    if not chosen:
        print("No valid recipes chosen.")
        return
    print("\nChosen recipes:")
    for r in chosen:
        print(f"- {r.name}")
    print("\nCombined grocery list:")
    all_ings: Dict[str, int] = {}
    for r in chosen:
        for ing in r.ingredients:
            all_ings[ing] = all_ings.get(ing, 0) + 1
    for ing, count in all_ings.items():
        prefix = f"{count}x " if count > 1 else ""
        print(f"- {prefix}{ing}")

def main():
    recipes = load_recipes()
    while True:
        print("\nRecipe Planner with Groceries")
        print("1. List recipes")
        print("2. Add recipe")
        print("3. Plan meals & grocery list")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            list_recipes(recipes)
        elif choice == "2":
            add_recipe(recipes)
        elif choice == "3":
            plan_meals(recipes)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
