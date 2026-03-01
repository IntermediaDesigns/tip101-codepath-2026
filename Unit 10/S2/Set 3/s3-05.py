# ------------------------------------------------
#  *                    Problem 5: Custom Sort String
#
#    Given two strings order and s, rearrange the characters of s so that
#    characters appearing in order come first, in the same relative order as
#    they appear in order. Characters not in order can go anywhere.
#    Return any valid permutation of s.

def custom_sort_string(order, s):
    pass


print(custom_sort_string("cba", "abcd"))
# Expected Output: "cbad" (or any valid arrangement like "dcba", "cdba", "cbda")
# "c", "b", "a" must appear before "d"

print(custom_sort_string("bcafg", "abcd"))
# Expected Output: "bcad" (or any valid arrangement where b, c, a appear in that order)

# ------------------------------------------------
