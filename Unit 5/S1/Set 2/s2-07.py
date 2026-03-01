# ------------------------------------------------
#  *                    Problem 7: Sum of Cards
#
#    Write a function sum_hand() that takes in an instance of Hand as a
#    parameter and returns the summed value of all cards in the hand.
#    If any card in the hand is invalid, return None.


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
        face_values = {"Ace": 1, "Jack": 11, "Queen": 12, "King": 13}
        if not self.is_valid():
            return None
        if self.rank in face_values:
            return face_values[self.rank]
        return int(self.rank)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)


def sum_hand(hand):
    pass


card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

total = sum_hand(hand)
print(total)

# Example Output:
# 17
#
# ------------------------------------------------
