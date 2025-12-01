import random
from dataclasses import dataclass

@dataclass
class Character:
    name: str
    hp: int
    attack_min: int
    attack_max: int

    def is_alive(self) -> bool:
        return self.hp > 0

    def attack(self, other: "Character") -> int:
        dmg = random.randint(self.attack_min, self.attack_max)
        other.hp = max(0, other.hp - dmg)
        return dmg

def player_turn(player: Character, enemy: Character):
    print(f"\nYour HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
    print("1. Attack")
    print("2. Heal (+10 HP)")
    choice = input("Choose: ")

    if choice == "2":
        player.hp += 10
        print("You healed 10 HP.")
    else:
        dmg = player.attack(enemy)
        print(f"You hit {enemy.name} for {dmg} damage!")

def enemy_turn(player: Character, enemy: Character):
    if not enemy.is_alive():
        return
    dmg = enemy.attack(player)
    print(f"{enemy.name} hits you for {dmg} damage!")

def main():
    player = Character(name="Hero", hp=100, attack_min=8, attack_max=16)
    enemy = Character(name="Goblin King", hp=80, attack_min=6, attack_max=14)

    print("⚔️  CLI RPG Battle ⚔️")
    while player.is_alive() and enemy.is_alive():
        player_turn(player, enemy)
        if enemy.is_alive():
            enemy_turn(player, enemy)

    if player.is_alive():
        print("\nYou defeated the Goblin King! 🎉")
    else:
        print("\nYou were defeated... 💀")

if __name__ == "__main__":
    main()
