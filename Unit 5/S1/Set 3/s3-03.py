# ------------------------------------------------
#  *                    Problem 3: Update Kart
#
#    Update player_one's kart from "Super Blooper" to "Dolphin Dasher".
#    Use get_player() before and after to verify the change.


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")
print(player_one.get_player())

# Update kart here
# player_one.??? = ???

print(player_one.get_player())

# Example Output:
# Yoshi driving the Super Blooper
# Yoshi driving the Dolphin Dasher
#
# ------------------------------------------------
