# ------------------------------------------------
#  *                    Problem 2: 3-Node Sum I
#
#    Given the root of a binary tree that has EXACTLY 3 nodes (root, left child,
#    right child), return True if the value of the root equals the sum of its two
#    children. Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_tree(root):
    pass


# Example Input Tree #1:
#      10
#     /  \
#    4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2:
#      5
#     / \
#    3   1
# Input: root = 5
# Expected Output: False
#
# ------------------------------------------------
