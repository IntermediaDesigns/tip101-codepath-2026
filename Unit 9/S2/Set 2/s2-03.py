# ------------------------------------------------
#  *                    Problem 3: Maximum Nodes at Any Level in Binary Tree
#
#    Given the root of a binary tree, return the maximum number of nodes
#    in any level of the binary tree.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_max(root):
    pass


# Example Input Tree #1:
#      4
#     / \
#    2   6
#   / \
#  1   3

root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

print(level_max(root1))

# Example Output: 2
# Levels 2 & 3 each have 2 nodes

# Example Input Tree #2:
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

print(level_max(root2))

# Example Output: 4
# Level 3 has 4 nodes, the most of any level
#
# ------------------------------------------------
