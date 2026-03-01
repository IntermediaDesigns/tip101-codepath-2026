# ------------------------------------------------
#  *                    Problem 7: Race Results
#
#    Given a list race_results of Player objects where the first player came
#    first, second came second, etc., write a function print_results() that
#    prints each player's placement and character name.


class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def get_player(self):
        return f"{self.character} driving the {self.kart}"


def print_results(race_results):
    pass


peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")

race_one = [peach, mario, luigi]
print_results(race_one)

# Example Output:
# 1. Peach
# 2. Mario
# 3. Luigi
#
# ------------------------------------------------
