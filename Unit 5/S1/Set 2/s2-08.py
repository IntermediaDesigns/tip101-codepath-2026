# ------------------------------------------------
#  *                    Problem 8: Print Hand
#
#    The Card class has been updated with a next attribute representing the
#    next card in a hand. Write a function print_hand() that accepts a Card
#    object and returns a list of all cards in the hand starting from that card.


class Card:
    def __init__(self, suit, rank, next=None):
        self.suit = suit
        self.rank = rank
        self.next = next


def print_hand(starting_card):
    pass


card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(print_hand(card_one))

# Example Output:
# [card_one, card_two, card_three]  (list of Card objects)
#
# ------------------------------------------------
