# ------------------------------------------------
#  *                    Problem 3: BST Insert
#
#    Given the root of a binary search tree, insert a new node with a given key
#    and value. Return the root of the modified tree. The tree is sorted by key.
#    If a node with the given key already exists, update its value.
#    You do not need to maintain a balanced tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def insert(root, key, value):
    pass


# Example Input Tree #1: (depicted by keys)
#        10
#       /  \
#      5    15
#     / \
#    1   6
# Input: root = 10, key = 9, value = 'Naruto'
# Expected Output Tree:
#        10
#       /  \
#      5    15
#     / \
#    1   6
#         \
#          9

# Example Input Tree #2: Empty Tree (None)
# Input: root = None, key = 4, value = "Sailor Moon"
# Expected Output Tree:
#    4
#
# ------------------------------------------------
