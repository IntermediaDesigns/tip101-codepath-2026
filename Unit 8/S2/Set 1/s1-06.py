# ------------------------------------------------
#  *                    Problem 6: Merge Binary Trees
#
#    Given two binary trees root1 and root2, merge them into a new tree.
#    Merge rule: if two nodes overlap, sum their values as the new node's value.
#    If only one node exists at a position, use that node as-is.
#    Return the root of the merged tree.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    pass


# Example Input Trees:
#      1          2
#     / \        / \
#    3   2      1   3
#   /             \
#  5               4     7
#
# Input: root1 = 1, root2 = 2
# Expected Output Tree:
#        3
#       / \
#      4   5
#     / \   \
#    5   4   7
#
# ------------------------------------------------
