# ------------------------------------------------
#  *                    Problem 2: Print Card
#
#    Step 1: The print_card() method has been added to the Card class below.
#    Step 2: Create an instance of Card in a variable named card with
#            suit "Clubs" and rank "Ace".
#    Step 3: Call print_card() on your card instance.


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")


# Create your card here
card = None  # Replace with your code
# card.print_card()  # Uncomment after instantiating

# Example Output:
# Ace of Clubs
#
# ------------------------------------------------
