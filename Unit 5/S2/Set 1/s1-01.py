# ------------------------------------------------
#  *                    Problem 1: Battle Pokemon
#
#    Write a method attack() that takes in a Pokemon object opponent and
#    decreases opponent's hp by self's damage amount.
#    - If opponent's hp drops to 0 or below, set it to 0 and print
#      "<Opponent name> fainted"
#    - Otherwise, print "<Pokemon name> dealt <damage> damage to <opponent name>"


class Pokemon:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp        # hit points
        self.damage = damage  # damage this pokemon does to its opponent

    def attack(self, opponent):
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            opponent.hp = 0
            print(f"{opponent.name} fainted")
        else:
            print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30)

pikachu.attack(bulbasaur)
bulbasaur.attack(pikachu)


# Example Output:
# Pikachu dealt 20 damage to Bulbasaur
# Bulbasaur dealt 30 damage to Pikachu
#
# ------------------------------------------------
