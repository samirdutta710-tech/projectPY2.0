from dataclasses import dataclass, field

@dataclass
class Room:
    name: str
    description: str
    exits: dict  # direction -> room_name
    item: str | None = None

@dataclass
class Player:
    current_room: str
    inventory: list[str] = field(default_factory=list)

def create_world():
    return {
        "hall": Room(
            name="hall",
            description="You are in a hall. There is a door to the east.",
            exits={"east": "kitchen"},
            item="key",
        ),
        "kitchen": Room(
            name="kitchen",
            description="You are in a kitchen. There is a door to the west and south.",
            exits={"west": "hall", "south": "cellar"},
            item=None,
        ),
        "cellar": Room(
            name="cellar",
            description="It's dark and creepy here. There is a door to the north.",
            exits={"north": "kitchen"},
            item="treasure",
        ),
    }

def describe_room(room: Room, player: Player):
    print(f"\n== {room.name.upper()} ==")
    print(room.description)
    if room.item and room.item not in player.inventory:
        print(f"You see a {room.item} here.")
    print("Exits:", ", ".join(room.exits.keys()))

def main():
    world = create_world()
    player = Player(current_room="hall")

    print("Welcome to the Tiny Adventure!")
    while True:
        room = world[player.current_room]
        describe_room(room, player)

        command = input("\nWhat do you do? ").strip().lower()

        if command in {"quit", "exit"}:
            print("Goodbye!")
            break

        if command.startswith("go "):
            direction = command.split(" ", 1)[1]
            if direction in room.exits:
                player.current_room = room.exits[direction]
            else:
                print("You can't go that way.")
        elif command.startswith("take "):
            item_name = command.split(" ", 1)[1]
            if room.item == item_name and item_name not in player.inventory:
                player.inventory.append(item_name)
                print(f"You take the {item_name}.")
            else:
                print("You can't take that.")
        elif command == "inventory":
            if player.inventory:
                print("You have:", ", ".join(player.inventory))
            else:
                print("You are carrying nothing.")
        else:
            print("I don't understand that command.")

        if "treasure" in player.inventory and player.current_room == "hall":
            print("\nYou return to the hall with the treasure. You win! 🎉")
            break

if __name__ == "__main__":
    main()
