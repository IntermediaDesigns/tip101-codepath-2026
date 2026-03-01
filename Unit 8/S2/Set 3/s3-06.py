# ------------------------------------------------
#  *                    Problem 6: Nested Binary Trees
#
#    Given the roots of two binary trees root and sub_root, return True if
#    there is a subtree of root with the same structure and node values as
#    sub_root. Return False otherwise.
#
#    A subtree consists of a node and all of its descendants. The tree itself
#    is also considered a subtree of itself.
#
#    Evaluate the time complexity of your solution.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_subtree(root, sub_root):
    pass


# Example Input Trees #1:
#        2          3
#       / \        / \
#      3   5      6   7
#     / \   \
#    6   7   12
# Input: root = 2, sub_root = 3 -> Expected Output: True
# Explanation: The subtree rooted at 3 in root matches sub_root exactly.

# Example Input Trees #2:
#        2          3
#       / \        / \
#      3   5      1   2
#     / \   \
#    6   7   12
# Input: root = 2, sub_root = 3 -> Expected Output: False
#
# ------------------------------------------------
