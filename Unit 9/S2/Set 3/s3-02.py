# ------------------------------------------------
#  *                    Problem 2: Node Values Between Given Levels in Binary Tree
#
#    Given the root of a binary tree, return a list of all node values between
#    start_level and end_level (inclusive).
#    You may assume 1 <= start_level <= end_level <= tree depth.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_level_range(root, start_level, end_level):
    pass


# Example Input Tree:
#           3
#          / \
#         5   1
#        / \ / \
#       6  2 0  8
#         / \
#        7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(get_level_range(root, 2, 4))

# Example Output: [5, 1, 6, 2, 0, 8, 7, 4]
# Level 2 nodes: 5, 1
# Level 3 nodes: 6, 2, 0, 8
# Level 4 nodes: 7, 4
#
# ------------------------------------------------
