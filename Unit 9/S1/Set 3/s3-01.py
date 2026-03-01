# ------------------------------------------------
#  *                    Problem 1: Evaluate Mathematical Expression Tree
#
#    You are given the root of a FULL binary tree with these properties:
#      - Leaf nodes have an integer value
#      - Non-leaf nodes have a string value: "+", "-", "*", or "/"
#
#    Evaluation rules:
#      - Leaf node: return its integer value
#      - Non-leaf node: evaluate both children and apply the math operation
#
#    Return the result of evaluating the root node.
#    A full binary tree has nodes with either 0 or 2 children.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate_tree(root):
    pass


# Example Input Tree:
#        '+'
#        /  \
#       '*'  '-'
#      / \   / \
#     5   2 60  20
#
# Input: root = '+'
# Expected Output: 50
# Explanation: (5 * 2) + (60 - 20) = 10 + 40 = 50
#
# ------------------------------------------------
