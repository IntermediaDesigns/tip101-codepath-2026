# ------------------------------------------------
#  *                    Problem 3: Verify Update
#
#    Using the Card class from Problem 2, update card's suit from "Clubs" to
#    "Hearts". Use print_card() to verify the update.


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")


card = Card("Clubs", "Ace")
card.print_card()

# Update suit here
# card.??? = ???

card.print_card()

# Example Output:
# Ace of Clubs
# Ace of Hearts
#
# ------------------------------------------------
