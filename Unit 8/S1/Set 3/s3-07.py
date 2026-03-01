# ------------------------------------------------
#  *                    Problem 7: Binary Tree All Lesser
#
#    Given the root of a binary tree and a value val, write a function is_lesser()
#    that returns True if ALL nodes in the tree have a value less than val.
#    If the tree is empty, return False.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_lesser(root, val):
    pass


# Example Input Tree:
#        4
#       / \
#      2   5
#     / \
#    1   3

# Input: root = 4, val = 5 -> Expected Output: False  (5 is not < 5)
# Input: root = 4, val = 6 -> Expected Output: True
#
# ------------------------------------------------
