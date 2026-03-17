# ------------------------------------------------
#  *                    Problem 4: Make Palindromes
#
#    You are given a string s of lowercase English letters. In one operation,
#    you can replace any character with another lowercase English letter.
#    Write a function make_palindrome() that turns s into a palindrome using the
#    minimum number of operations. If multiple palindromes can be made with the
#    same minimum operations, return the lexicographically smallest one.


def make_palindrome(s):
    pass


s = "egcfe"
print(make_palindrome(s))
# "efcfe" — change 'g' to 'f' (1 operation)

s2 = "abcd"
print(make_palindrome(s2))
# "abba" — change 'c' to 'b' and 'd' to 'a' (2 operations)

s3 = "seven"
print(make_palindrome(s3))
# "neven" — change 's' to 'n' (1 operation)

# Example Output:
# efcfe
# abba
# neven
#
# ------------------------------------------------
