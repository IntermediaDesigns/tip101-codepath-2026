# ------------------------------------------------
#  *                    Problem 2: Sum of Node Values by Level in Binary Tree
#
#    Given the root of a binary tree, return a list of the sums of node values
#    in each level of the binary tree.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_sum(root):
    pass


# Example Input Tree:
#      4
#     / \
#    2   6
#   / \
#  1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(level_sum(root))

# Example Output: [4, 8, 4]
# Level 1: 4
# Level 2: 2 + 6 = 8
# Level 3: 1 + 3 = 4
#
# ------------------------------------------------
