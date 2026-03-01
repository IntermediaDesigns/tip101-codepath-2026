# ------------------------------------------------
#  *                    Problem 3: BST Insert III
#
#    Given the root of a BST, insert a new node with a given value. Return the
#    root of the modified tree. If a node with the given value already exists,
#    place the new node in the LEFT subtree.
#    You do not need to maintain a balanced tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def insert_with_duplicates(root, value):
    pass


# Example Input Tree #1:
#        10
#       /  \
#      8    15
#     / \
#    1   6
# Input: root = 10, value = 9
# Expected Output Tree: 9 inserted as right child of 6

# Example Input Tree #2: same tree, value = 8 (duplicate)
# Expected Output Tree: new 8 inserted in LEFT subtree of existing 8

# Example Input Tree #3: Empty Tree
# Input: root = None, value = 4
# Expected Output Tree: single node with value 4
#
# ------------------------------------------------
