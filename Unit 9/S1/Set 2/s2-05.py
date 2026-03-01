# ------------------------------------------------
#  *                    Problem 5: Transformable Binary Trees by Swapping Subtrees
#
#    Given the roots of two binary trees root1 and root2, write a function
#    can_swap() that returns True if root1 can be transformed into root2 by
#    doing any number of left/right child swaps at any node.
#    Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def can_swap(root1, root2):
    pass


# Example Input Trees:
#
#   root1:           root2:
#       6                6
#      / \              / \
#     3   8            8   3
#    / \ / \          / \ / \
#   1  7 4  2        2  4 7  1
#  / \   \  /       / \   \  /
# 7   1   3 3      3   1   1 7
#                  (mirrored at each level)
#
# Input: root1 = 6, root2 = 6
# Expected Output: True
# Explanation: Swapping left/right children at each level of root1 produces root2.
#
# ------------------------------------------------
