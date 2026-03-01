# ------------------------------------------------
#  *                    Problem 2: Find Minimum Depth of Binary Tree
#
#    Given the root of a binary tree, return its minimum depth.
#    The minimum depth is the number of nodes along the shortest path
#    from the root down to the nearest leaf node.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def min_depth(root):
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

print(min_depth(root1))

# Example Output: 2
# Shortest path: 3 -> 9 (2 nodes)

# Example Input Tree #2:
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)

print(min_depth(root2))

# Example Output: 5
#
# ------------------------------------------------
