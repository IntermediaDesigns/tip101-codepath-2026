# ------------------------------------------------
#  *                    Problem 4: Find Leftmost Path I
#
#    Given the root of a binary tree, write a function left_path() that returns
#    a list of the values along the leftmost path of the tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def left_path(root):
    pass


# Example Input Tree #1:
#        1
#       / \
#      2   5
#     / \
#    4   3
# Input: root = 1 -> Expected Output: [1, 2, 4]

# Example Input Tree #2:
#    1
#     \
#      2
#     /
#    3
# Input: root = 1 -> Expected Output: [1]

# Input: root = None -> Output: []
#
# ------------------------------------------------
