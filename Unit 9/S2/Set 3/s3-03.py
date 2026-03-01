# ------------------------------------------------
#  *                    Problem 3: Cousins in Binary Tree
#
#    Given the root of a binary tree with unique values and the values of two
#    different nodes x and y, return True if x and y are cousins, False otherwise.
#    Two nodes are cousins if they have the same depth but different parents.
#    The root node is at depth 0; children of depth k are at depth k+1.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_cousins(root, x, y):
    pass


# Example Input Tree #1:
#      1
#     / \
#    2   3
#   /
#  4

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

print(is_cousins(root1, 4, 3))
# Example Output: False

# Example Input Tree #2:
#      1
#     / \
#    2   3
#     \   \
#      4   5

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(5)

print(is_cousins(root2, 5, 4))
# Example Output: True

# Example Input Tree #3 (same tree as above):
print(is_cousins(root2, 2, 3))
# Example Output: False (same depth, but siblings share the same parent)
#
# ------------------------------------------------
