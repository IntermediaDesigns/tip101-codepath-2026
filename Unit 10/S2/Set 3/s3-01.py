# ------------------------------------------------
#  *                    Problem 1: Count of Matches in Tournament
#
#    Given n teams in a tournament:
#    - If teams is even: n/2 matches played, n/2 teams advance.
#    - If teams is odd: (n-1)/2 matches played, (n-1)/2 + 1 teams advance.
#    Return the total number of matches played until a winner is decided.

def number_of_matches(n):
    pass


print(number_of_matches(7))   # Expected Output: 6
# Round 1: 3 matches, Round 2: 2 matches, Round 3: 1 match -> 6 total

print(number_of_matches(14))  # Expected Output: 13
# Round 1: 7, Round 2: 3, Round 3: 2, Round 4: 1 -> 13 total

# ------------------------------------------------
