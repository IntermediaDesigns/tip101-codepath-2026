# ------------------------------------------------
#  *                    Problem 4: Valid Card
#
#    Update the Card class with a method is_valid() that takes no parameters
#    except self. Return True if the suit and rank are both valid values,
#    otherwise return False.
#    Valid suits: "Hearts", "Spades", "Clubs", "Diamonds"
#    Valid ranks: "2"-"10", "Jack", "Queen", "King", "Ace"


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        pass


my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())

# Example Output:
# True
# False
#
# ------------------------------------------------
