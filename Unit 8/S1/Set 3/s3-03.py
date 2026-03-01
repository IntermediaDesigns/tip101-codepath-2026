# ------------------------------------------------
#  *                    Problem 3: 3-Node Equality
#
#    You are given the root of a binary tree that has AT MOST 3 nodes.
#    Return True if the root's children have equal values. Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def equality(root):
    pass


# Example Input Tree #1:
#      1
#     / \
#    2   2
# Input: root = 1 -> Expected Output: True

# Example Input Tree #2:
#      1
#     /
#    2
# Input: root = 1 -> Expected Output: False
#
# ------------------------------------------------
