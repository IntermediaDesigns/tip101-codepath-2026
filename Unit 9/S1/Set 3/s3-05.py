# ------------------------------------------------
#  *                    Problem 5: Replace Node Value with Sum of Subtree
#
#    Given a binary tree, in-place replace each node's value with the sum of
#    all elements in its left and right subtrees. Treat an empty child as 0.
#
#    Return the root of the modified tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_transform(root):
    pass


# Example Input Tree:
#        1
#       / \
#      2   3
#       \  / \
#        4 5  6
#         / \
#        7   8
#
# Input: root = 1
# Expected Output Tree (root val = 35):
#        35
#       /  \
#      4    26
#       \   / \
#        0 15   0
#         / \
#        0   0
#
# Explanation: Each node's new value = sum of all values in its subtrees.
#   Node 4's subtree is empty -> 0
#   Node 5's subtree is {7,8} -> 15
#   Node 6's subtree is empty -> 0
#   Node 2's subtree is {4} -> 4
#   Node 3's subtree is {5,6,7,8} -> 26
#   Node 1's subtree is all other nodes -> 35
#
# ------------------------------------------------
