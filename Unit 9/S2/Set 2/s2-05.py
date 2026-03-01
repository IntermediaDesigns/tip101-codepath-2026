# ------------------------------------------------
#  *                    Problem 5: Find the Diameter of Binary Tree
#
#    Given the root of a binary tree, return the length of the diameter of the tree.
#    The diameter is the length of the longest path between any two nodes.
#    This path may or may not pass through the root.
#    Length is measured by the number of edges between nodes.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_diameter(root):
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

print(find_diameter(root))

# Example Output: 3
# Longest path: [4, 2, 1, 3] or [5, 2, 1, 3] (3 edges)
#
# ------------------------------------------------
