# ------------------------------------------------
#  *                    Problem 4: Set Character
#
#    Update the Player class with a method set_character() that takes in one
#    parameter name.
#    - If name is valid, update the character attribute and print "Character updated".
#    - Otherwise, print "Invalid character".
#    Valid names: "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario",
#                 "Donkey Kong", "Bowser"


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"

    def set_character(self, name):
        pass


player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")

player_one.set_character("Peach")
player_two.set_character("Kermit")

# Example Output:
# Character updated
# Invalid character
#
# ------------------------------------------------
