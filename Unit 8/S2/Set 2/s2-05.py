# ------------------------------------------------
#  *                    Problem 5: BST In-order Predecessor
#
#    The in-order predecessor of a node is the node with the largest key
#    LESS THAN the key of the given node.
#
#    Given the root of a BST and a TreeNode current, write a function that
#    returns the in-order predecessor of current. Assume the tree is balanced.
#
#    Evaluate the time complexity of your solution.


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def inorder_predecessor(root, current):
    pass


# Example Input Tree #1: (depicted by keys)
#        10
#       /  \
#      5    15
#     / \
#    2   8
#   / \
#  1   3
# Input: root = 10, current = node(key=5) -> Expected: node with key 3

# Example Input Tree #2: (depicted by keys)
#        10
#       /  \
#      5    15
#     / \
#    1   8
#       / \
#      6   9
# Input: root = 10, current = node(key=9) -> Expected: node with key 8
#
# ------------------------------------------------
