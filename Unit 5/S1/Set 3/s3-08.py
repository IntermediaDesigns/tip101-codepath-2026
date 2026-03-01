# ------------------------------------------------
#  *                    Problem 8: Get Rank
#
#    The Player class has been updated with an ahead attribute representing
#    the player directly ahead in the race. Write a function get_place() that
#    accepts a Player object and returns their current place number in the race.


class Player:
    def __init__(self, character, kart, opponent=None):
        self.character = character
        self.kart = kart
        self.items = []
        self.ahead = opponent


def get_place(my_player):
    pass


peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place(luigi)
print(player1_rank)

player2_rank = get_place(peach)
print(player2_rank)

player3_rank = get_place(mario)
print(player3_rank)

# Example Output:
# 3
# 1
# 2
#
# ------------------------------------------------
