# ------------------------------------------------
#  *                    Problem 1: Poker Two-Pair Hand
#
#    Write a function is_two_pair() that takes in a list player_hand of 5 Card
#    objects and returns True if the player has a two-pair hand (two cards of
#    one rank and two cards of another rank), False otherwise.


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def is_two_pair(player_hand):
    pass


card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

# Example Output:
# True   (Two Aces + Two 4s + unused 6)
# False  (Only one pair: two 4s)
#
# ------------------------------------------------
