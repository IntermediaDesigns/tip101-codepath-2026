# ------------------------------------------------
#  *                    Problem 6: Print Inventory
#
#    Update the Player class with a method print_inventory() that accepts no
#    parameters except self. Print the name and quantity of each item in the
#    player's items list. If the player has no items, print "Inventory empty".


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def add_item(self, item_name):
        valid_items = {"banana", "green shell", "red shell", "bob-omb",
                       "super star", "lightning", "bullet bill"}
        if item_name in valid_items:
            self.items.append(item_name)

    def print_inventory(self):
        pass


player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]

player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()

# Example Output:
# Inventory: banana: 2, bob-omb: 1, super star: 1
# Inventory empty
#
# ------------------------------------------------
