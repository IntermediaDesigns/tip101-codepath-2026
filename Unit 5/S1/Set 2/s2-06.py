# ------------------------------------------------
#  *                    Problem 6: Hand Class
#
#    A Hand class has been added below. Implement two methods:
#    - add_card(card): adds a Card object to the hand
#    - remove_card(card): removes a Card object from the hand


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
        pass

    def remove_card(self, card):
        pass


card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")
player1_hand = Hand()
# cards = []
player1_hand.add_card(card_one)
# cards = [card_one]
player1_hand.add_card(card_two)
# cards = [card_one, card_two]
player1_hand.remove_card(card_one)
# cards = [card_two]
print(len(player1_hand.cards))  # Should be 1

# Example: After add/remove, hand should contain only card_two
#
# ------------------------------------------------
