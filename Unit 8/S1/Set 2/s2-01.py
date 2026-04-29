# ------------------------------------------------
#  *                    Problem 1: Build a Binary Tree II
#
#    Given the TreeNode class below, create a binary tree where:
#      - Root has value 5
#      - Left child has value 10
#      - Right child has value 20
#
#         5
#        / \
#       10  20


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# Build the tree here:
root = TreeNode(5)  # Replace with your implementation
node_left = TreeNode(10)
node_right = TreeNode(20)

root.left = node_left
root.right = node_right

# ------------------------------------------------
