# ------------------------------------------------
#  *                    Problem 2: Get Player
#
#    Step 1: The get_player() method has been added to the Player class below.
#    Step 2: Create a second Player instance named player_two with character
#            "Bowser" and kart "Pirahna Prowler".
#    Step 3: Print the string:
#            "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


player_one = Player("Yoshi", "Super Blooper")

# Create player_two here
player_two = None  # Replace with your code

# Print the match string here
# print(???)

# Example Output:
# Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler
#
# ------------------------------------------------
