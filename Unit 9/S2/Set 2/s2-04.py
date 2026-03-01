# ------------------------------------------------
#  *                    Problem 4: Vertical Order Traversal of Binary Tree
#
#    Given the root of a binary tree, return the vertical order traversal of
#    its nodes' values (from top to bottom, column by column).
#    If two nodes are in the same row and column, order from left to right.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def vertical_order(root):
    pass


# Example Input Tree #1:
#      3
#     / \
#    9  20
#       / \
#      15   7

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(vertical_order(root1))

# Example Output: [[9], [3, 15], [20], [7]]

# Example Input Tree #2:
#        3
#       / \
#      9   8
#     / \ / \
#    4  0 1  7

root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(8)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(0)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(7)

print(vertical_order(root2))

# Example Output: [[4], [9], [3, 0, 1], [8], [7]]
#
# ------------------------------------------------
