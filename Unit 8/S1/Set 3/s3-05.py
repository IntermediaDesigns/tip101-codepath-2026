# ------------------------------------------------
#  *                    Problem 5: Find Leftmost Path II
#
#    If you implemented left_path() iteratively in Problem 4, implement it
#    recursively here. If you implemented it recursively, implement it iteratively.
#
#    Evaluate the time complexity of your implementation.


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
