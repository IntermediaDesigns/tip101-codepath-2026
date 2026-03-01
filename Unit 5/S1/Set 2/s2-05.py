# ------------------------------------------------
#  *                    Problem 5: Get Value
#
#    Update the Card class with a method get_value() that takes no parameters
#    except self. Return the card's numeric value based on its rank:
#    - "2"-"10"  → return as integer
#    - "Ace"     → return 1
#    - "Jack"    → return 11
#    - "Queen"   → return 12
#    - "King"    → return 13
#    - Invalid   → return None


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        valid_suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
        valid_ranks = {"2", "3", "4", "5", "6", "7", "8", "9", "10",
                       "Jack", "Queen", "King", "Ace"}
        return self.suit in valid_suits and self.rank in valid_ranks

    def get_value(self):
        pass


card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())

# Example Output:
# 7
# 11
#
# ------------------------------------------------
