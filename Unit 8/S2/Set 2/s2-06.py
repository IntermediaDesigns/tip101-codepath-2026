# ------------------------------------------------
#  *                    Problem 6: Identical Binary Trees
#
#    Given the roots of two binary trees root1 and root2, write a function
#    is_identical() that returns True if they are structurally identical and
#    all corresponding nodes have the same values. Return False otherwise.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_identical(root1, root2):
    pass


# Example Input Trees #1:
#    1      1
#   / \    / \
#  2   3  2   3
# Input: root1 = 1, root2 = 1 -> Expected Output: True

# Example Input Trees #2:
#    1      1
#   /        \
#  2          2
# Input: root1 = 1, root2 = 1 -> Expected Output: False

# Example Input Trees #3:
#    1      1
#   / \    / \
#  2   1  1   2
# Input: root1 = 1, root2 = 1 -> Expected Output: False
#
# ------------------------------------------------
