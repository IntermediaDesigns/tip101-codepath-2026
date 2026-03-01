# ------------------------------------------------
#  *                    Problem 3: Valid Word Abbreviation
#
#    A string can be abbreviated by replacing non-adjacent, non-empty substrings
#    with their lengths (no leading zeros allowed).
#    Given a string word and an abbreviation abbr, return True if the string
#    matches the abbreviation, False otherwise.

def valid_word_abbreviation(word, abbr):
    pass


print(valid_word_abbreviation("internationalization", "i12iz4n"))
# Expected Output: True
# "i" + 12 chars + "iz" + 4 chars + "n"

print(valid_word_abbreviation("apple", "a2e"))
# Expected Output: False
# "a" + 2 chars + "e" would be "appe" != "apple"

# ------------------------------------------------
