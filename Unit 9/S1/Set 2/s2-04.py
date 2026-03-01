# ------------------------------------------------
#  *                    Problem 4: Second Minimum Value in a Special Binary Tree
#
#    You are given a non-empty special binary tree where every node has exactly
#    0 or 2 children. If a node has two children, its value is the SMALLER of
#    its two children's values (root.val == min(left.val, right.val)).
#
#    Return the second minimum value across all nodes. If no second minimum
#    exists, return -1.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_second_minimum_value(root):
    pass


# Example Input Tree #1:
#      2
#     / \
#    2   5
#       / \
#      5   7
# Input: root = 2
# Expected Output: 5
# Explanation: Smallest = 2, second smallest = 5.

# Example Input Tree #2:
#    2
#   / \
#  2   2
# Input: root = 2
# Expected Output: -1
# Explanation: Smallest = 2, no second smallest exists.
#
# ------------------------------------------------
