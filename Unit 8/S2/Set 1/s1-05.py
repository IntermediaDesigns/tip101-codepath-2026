# ------------------------------------------------
#  *                    Problem 5: BST In-order Successor
#
#    The in-order successor of a node is the node with the smallest key
#    GREATER THAN the key of the given node.
#
#    Given the root of a BST and a TreeNode current, write a function that
#    returns the in-order successor of current. Assume the tree is balanced.
#
#    Evaluate the time complexity of your solution.


class TreeNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def inorder_successor(root, current):
    pass


# Build Example Tree:
#        10
#       /  \
#      5    15
#     / \
#    1   8
#       / \
#      6   9

n1 = TreeNode(1)
n6 = TreeNode(6)
n9 = TreeNode(9)
n8 = TreeNode(8, left=n6, right=n9)
n5 = TreeNode(5, left=n1, right=n8)
n15 = TreeNode(15)
n10 = TreeNode(10, left=n5, right=n15)  # root

# Example 1: current = n5 (key=5) -> Expected: node with key 6
# Example 2: current = n6 (key=6) -> Expected: node with key 8
#
# ------------------------------------------------
