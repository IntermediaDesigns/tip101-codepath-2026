# ------------------------------------------------
#  *                    Problem 2: Find Lonely Nodes
#
#    Given the root of a binary tree, return a list containing the values of
#    all lonely nodes in any order.
#
#    A lonely node is a node that is the ONLY child of its parent.
#    The root is NOT lonely (it has no parent).
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_lonely_nodes(root):
    pass


# Example Input Tree #1:
#      1
#     / \
#    2   3
#     \
#      4
# Input: root = 1 -> Expected Output: [4]

# Example Input Tree #2:
#        7
#       / \
#      1   4
#     /   / \
#    6   5   3
#         \
#          2
# Input: root = 7 -> Expected Output: [6, 2]  (any order)

# Example Input Tree #3:
#        11
#       /  \
#      99  88
#     / \
#    77  66
#   / \
#  55  44
#  / \
# 33  22
# Input: root = 11 -> Expected Output: [77, 55, 33, 66, 44, 22]  (any order)
#
# ------------------------------------------------
