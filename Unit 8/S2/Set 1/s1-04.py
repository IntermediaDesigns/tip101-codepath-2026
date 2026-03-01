# ------------------------------------------------
#  *                    Problem 4: BST Remove I
#
#    Given a key and the root of a BST, remove the node with the given key.
#    Return the root of the modified tree. The tree is sorted by key.
#    If multiple nodes with the given key exist, remove the first one found.
#
#    For a node with TWO children: use the IN-ORDER SUCCESSOR (smallest node
#    in the right subtree) to replace the removed node.
#
#    Evaluate the time complexity of your function.
#
#    Pseudocode:
#    - Locate the node to be removed
#    - If the node is a leaf: remove it by redirecting its parent's child ref
#    - If the node has one child: replace the node with its child
#    - If the node has two children:
#        - Find the in-order successor (smallest node in right subtree)
#        - Swap the value of the node and its in-order successor
#        - Recursively remove the successor
#    - Return the root of the updated tree


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def remove_bst(root, key):
    pass


# Example Input Tree #1: (depicted by keys)
#        10
#       /  \
#      5    15
#     / \  /  \
#    1   8 13  16
# Input: root = 10, key = 10
# Expected Output Tree (root key = 13):
#        13
#       /  \
#      5    15
#     / \     \
#    1   8    16

# Example Input Tree #2: (depicted by keys)
#        10
#       /  \
#      5    15
#     / \  /  \
#    1   8 13  16
#         \
#          9
# Input: root = 10, key = 8
# Expected Output Tree (root key = 10):
#        10
#       /  \
#      5    15
#     / \  /  \
#    1   9 13  16

# Example Input Tree #3: same tree, key = 9 (leaf removal)
# Expected Output Tree: 9 is simply removed
#
# ------------------------------------------------
