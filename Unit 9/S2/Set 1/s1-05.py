# ------------------------------------------------
#  *                    Problem 5: Sum of Binary Tree Node Tilts
#
#    Given the root of a binary tree, return the sum of every tree node's tilt.
#    The tilt of a node is the absolute difference between the sum of all left
#    subtree node values and all right subtree node values.
#    If a node has no left or right child, that side's sum is treated as 0.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_tilt(root):
    pass


# Example Input Tree #1:
#      1
#     / \
#    2   3

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

print(find_tilt(root1))

# Example Output: 1
# Tilt of node 2: |0 - 0| = 0
# Tilt of node 3: |0 - 0| = 0
# Tilt of node 1: |2 - 3| = 1
# Sum: 0 + 0 + 1 = 1

# Example Input Tree #2:
#        4
#       / \
#      2   9
#     / \   \
#    3   5   7

root2 = TreeNode(4)
root2.left = TreeNode(2)
root2.right = TreeNode(9)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(7)

print(find_tilt(root2))

# Example Output: 15
#
# ------------------------------------------------
