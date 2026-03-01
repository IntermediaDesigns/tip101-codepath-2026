# ------------------------------------------------
#  *                    Problem 5: Equal Tree Split
#
#    Given the root of a binary tree, return True if removing ONE edge between
#    two nodes can split the tree into two trees with an equal number of nodes.
#    Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def can_split(root):
    pass


# Example Input Tree #1:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   7
# Input: root = 1
# Expected Output: True
# Explanation: Removing edge between 1 and 2 gives two trees of size 3 each.

# Example Input Tree #2:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
# Input: root = 1
# Expected Output: False
# Explanation: No single edge removal produces two equal-size trees (total = 7 nodes, odd)
#
# ------------------------------------------------
