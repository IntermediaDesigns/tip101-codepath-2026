# ------------------------------------------------
#  *                    Problem 6: Post-order Traversal
#
#    Given the root of a binary tree, return a list representing the postorder
#    traversal of its nodes' values.
#    Postorder: left subtree -> right subtree -> current node
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def postorder_traversal(root):
    pass


# Example Input Tree #1:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
# Input: root = 1 -> Expected Output: [4, 5, 2, 6, 3, 1]

# Input: root = None -> Output: []

# Example Input Tree #2:
#    1
# Input: root = 1 -> Output: [1]
#
# ------------------------------------------------
