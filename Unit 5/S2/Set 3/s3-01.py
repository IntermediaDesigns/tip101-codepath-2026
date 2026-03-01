# ------------------------------------------------
#  *                    Problem 1: Calculate Tournament Placement
#
#    Write a method get_tournament_place() that takes in opponents, a list of
#    other Player objects, and returns the current player's overall tournament
#    place. Rank is determined by lowest average race outcome (1st is best).


class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.race_outcomes = outcomes

    def get_tournament_place(self, opponents):
        pass


player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")

# Example Output:
# Mario was number 1
# (Mario avg: 1.6, Luigi avg: 2.0, Peach avg: 2.4)
#
# ------------------------------------------------
