# ------------------------------------------------
#  *                    Problem 5: BST Find Floor
#
#    Given a value and the root of a BST, write a function find_floor() that
#    finds the largest value in the BST that is less than or equal to the given
#    value. If no such node exists, return None.
#    Assume the tree is balanced.
#
#    Evaluate the time complexity of your solution.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_floor(root, value):
    pass


# Example: BST with values [1, 2, 5, 8, 10, 11, 12, 19]
# find_floor(root, 5)  -> 5   (5 exists in tree)
# find_floor(root, 7)  -> 5   (largest value <= 7 is 5)
# find_floor(root, 0)  -> None (no value <= 0 in tree)
#
# ------------------------------------------------
