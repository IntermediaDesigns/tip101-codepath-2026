# ------------------------------------------------
#  *                    Problem 5: Add Special Item
#
#    Update the Player class with a method add_item() that takes in one
#    parameter item_name. If the item is valid, add it to the player's items
#    list. The method does not return any value.
#    Valid items: "banana", "green shell", "red shell", "bob-omb",
#                 "super star", "lightning", "bullet bill"


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_character(self, name):
        valid_names = {"Mario", "Luigi", "Peach", "Yoshi", "Toad",
                       "Wario", "Donkey Kong", "Bowser"}
        if name in valid_names:
            self.character = name
            print("Character updated")
        else:
            print("Invalid character")

    def add_item(self, item_name):
        pass


player_one = Player("Yoshi", "Dolphin Dasher")
# items = []
player_one.add_item("red shell")
# items = ["red shell"]
player_one.add_item("super star")
# items = ["red shell", "super star"]
player_one.add_item("super smash")
# items = ["red shell", "super star"] — invalid, not added

print(player_one.items)

# Example Output:
# ['red shell', 'super star']
#
# ------------------------------------------------
