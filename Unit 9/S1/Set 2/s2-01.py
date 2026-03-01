# ------------------------------------------------
#  *                    Problem 1: Evaluate Boolean Full Binary Tree
#
#    You are given the root of a FULL binary tree with these properties:
#      - Leaf nodes have a boolean value: True or False
#      - Non-leaf nodes have a string value: "OR" or "AND"
#
#    Evaluation rules:
#      - Leaf node: return its boolean value
#      - Non-leaf node: evaluate both children and apply the AND/OR operation
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
#        'OR'
#        /   \
#     True  'AND'
#            /  \
#          False True
#
# Input: root = 'OR'
# Expected Output: True
# Explanation: AND(False, True) = False; OR(True, False) = True
#
# ------------------------------------------------
