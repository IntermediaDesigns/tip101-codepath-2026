# ------------------------------------------------
#  *                    Problem 2: Find Corresponding Node in Cloned Tree
#
#    You are given the roots of two binary trees: original and cloned (an
#    exact copy), along with a TreeNode target that is a reference to a node
#    in the original tree.
#
#    Return a reference to the SAME node (by position) in the cloned tree.
#    You may not modify either tree or the target node.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_target_copy(original, cloned, target):
    pass


# Example 1:
# Tree: [7, 4, 3, null, null, 6, 19], target = node with val 3
# Output: the node in cloned with val 3

# Example 2:
# Tree: [7], target = node with val 7
# Output: the node in cloned with val 7

# Example 3:
# Tree: [8, null, 6, null, 5, null, 4, null, 3, null, 2, null, 1], target = node with val 4
# Output: the node in cloned with val 4
#
# ------------------------------------------------
