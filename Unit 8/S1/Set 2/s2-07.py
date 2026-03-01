# ------------------------------------------------
#  *                    Problem 7: Binary Tree Product
#
#    Given the root of a binary tree, write a function that returns the product
#    of all nodes' values in the tree. If the tree is empty, return 1.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def product_tree(root):
    pass


# Example Input Tree #1:
#        4
#       / \
#      2   5
#     / \
#    1   3
# Input: root = 4 -> Expected Output: 120  (4 * 2 * 5 * 1 * 3)

# Example Input Tree #2: Empty Tree
# Input: root = None -> Expected Output: 1
#
# ------------------------------------------------
