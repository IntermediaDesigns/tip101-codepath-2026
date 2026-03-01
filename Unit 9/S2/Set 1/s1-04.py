# ------------------------------------------------
#  *                    Problem 4: Level Order Traversal of Binary Tree with Nested Lists
#
#    Given the root of a binary tree, return the level order traversal of its
#    nodes' values as a list of lists, where each inner list contains the node
#    values of a single level (from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    pass


# Example Input Tree:
#      3
#     / \
#    9  20
#       / \
#      15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order(root))

# Example Output: [[3], [9, 20], [15, 7]]
#
# ------------------------------------------------
