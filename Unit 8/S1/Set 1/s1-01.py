# ------------------------------------------------
#  *                    Problem 1: Build a Binary Tree I
#
#    Given the TreeNode class below, create the binary tree depicted:
#
#         10
#        /  \
#       4    6
#
#    Instantiate nodes and link them together to build the tree.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build the tree here:
root = None

tree = TreeNode(10, TreeNode(4), TreeNode(6))
print(tree.val)
print(tree.left.val)
print(tree.right.val)

# ------------------------------------------------
