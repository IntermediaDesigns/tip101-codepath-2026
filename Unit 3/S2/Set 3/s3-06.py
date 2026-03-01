# ------------------------------------------------
#  *                    Problem 6: Flowerbed
#
#    Imagine a flowerbed where flowers cannot be planted in adjacent plots.
#    Write a function can_place_flowers() that takes in an integer list flowerbed
#    containing 0s and 1s (where 0 is an empty plot and 1 is a planted plot) and an
#    integer n representing the number of new flowers to be planted.
#    The function returns True if n new flowers can be planted without violating the
#    no-adjacent-flowers rule, and False otherwise.


def can_place_flowers(flowerbed, n):
    pass


flowerbed = [1, 0, 0, 0, 1]

approved = can_place_flowers(flowerbed, 1)
approved2 = can_place_flowers(flowerbed, 2)

print(approved)
print(approved2)

# Example Output:
# True
# False
#
# ------------------------------------------------
