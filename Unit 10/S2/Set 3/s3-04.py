# ------------------------------------------------
#  *                    Problem 4: Leaves of a Binary Tree
#
#    Given the root of a binary tree, repeatedly:
#      1. Collect all leaf nodes (left to right).
#      2. Remove all leaf nodes.
#    Repeat until the tree is empty.
#    Return a list of lists, where each inner list is one round of collected leaves.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_leaves(root):
    pass


# Example Input Tree:
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(find_leaves(root))
# Expected Output: [[4, 5, 3], [2], [1]]
# (order within each inner list may vary)

# ------------------------------------------------
