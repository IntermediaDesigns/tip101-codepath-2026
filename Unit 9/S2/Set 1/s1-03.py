# ------------------------------------------------
#  *                    Problem 3: Odd-Even Level Sum Difference in Binary Tree
#
#    Given the root of a binary tree, return the difference between the sum of
#    all node values in odd levels and sum of all node values in even levels.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_difference(root):
    pass


# Example Input Tree:
#        6
#       / \
#      3   8
#     /   / \
#    5   4   2
#       / \   \
#      1   7   3

root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(2)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(3)

print(level_difference(root))

# Example Output: -5
# Odd level sum:  6 + 5 + 4 + 2 = 17
# Even level sum: 3 + 8 + 1 + 7 + 3 = 22
# 17 - 22 = -5
#
# ------------------------------------------------
