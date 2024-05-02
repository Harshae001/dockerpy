import random

# Define a function to display the game instructions
def display_instructions():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a mysterious land full of adventure.")
    print("Your mission is to explore and survive.")
    print("Commands: go [direction], get [item], use [item], quit")

# Define a class for the player
class Player:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print("You picked up the", item)

    def use_item(self, item):
        if item in self.inventory:
            print("You used the", item)
            self.inventory.remove(item)
        else:
            print("You don't have the", item)

# Define a dictionary to represent the game map
game_map = {
    "start": {
        "description": "You are standing at the entrance of a dark cave.",
        "exits": {"north": "forest"},
        "items": ["torch"]
    },
    "forest": {
        "description": "You are in a dense forest.",
        "exits": {"south": "start", "east": "river"},
        "items": ["sword"]
    },
    "river": {
        "description": "You are at the edge of a fast-flowing river.",
        "exits": {"west": "forest", "east": "mountain"},
        "items": ["map"]
    },
    "mountain": {
        "description": "You are at the foot of a tall mountain.",
        "exits": {"west": "river", "north": "cave"},
        "items": []
    },
    "cave": {
        "description": "You are inside a dark cave.",
        "exits": {"south": "mountain"},
        "items": ["treasure"]
    }
}

# Define a function to handle player movement
def move(player, current_room, direction):
    if direction in game_map[current_room]["exits"]:
        new_room = game_map[current_room]["exits"][direction]
        print(game_map[new_room]["description"])
        return new_room
    else:
        print("You can't go that way.")
        return current_room

# Define a function to handle player actions
def handle_action(player, current_room, action, item):
    if action == "go":
        return move(player, current_room, item)
    elif action == "get":
        if item in game_map[current_room]["items"]:
            player.add_item(item)
            game_map[current_room]["items"].remove(item)
        else:
            print("There's no", item, "here.")
    elif action == "use":
        player.use_item(item)
    elif action == "quit":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid command.")

# Main game loop
def main():
    display_instructions()
    player = Player()
    current_room = "start"
    print(game_map[current_room]["description"])
    while True:
        action = input("> ").lower().split()
        if len(action) == 1:
            action.append("")
        current_room = handle_action(player, current_room, action[0], action[1])

# Run the game
if __name__ == "__main__":
    main()
