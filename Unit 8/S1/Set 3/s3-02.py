# ------------------------------------------------
#  *                    Problem 2: 3-Node Booleans
#
#    You are given the root of a binary tree that has EXACTLY 3 nodes. The left
#    and right children have boolean values (True or False). The root has a
#    string value of either "AND" or "OR".
#
#    Apply the boolean operation of the root to its two children.
#    Return True if the result is truthy, False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def tree_expression(root):
    pass


# Example Input Tree #1:
#      'OR'
#      /   \
#   True  False
# Input: root = 'OR' -> Expected Output: True

# Example Input Tree #2:
#      'AND'
#      /    \
#   True  False
# Input: root = 'AND' -> Expected Output: False
#
# ------------------------------------------------
