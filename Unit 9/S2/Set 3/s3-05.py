# ------------------------------------------------
#  *                    Problem 5: Lowest Common Ancestor in Binary Tree
#
#    Given the root of a binary tree, find the lowest common ancestor (LCA)
#    of two nodes p and q. The LCA is the lowest node t that has both p and q
#    as descendants. A node can be considered a descendant of itself.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_lca(root, p, q):
    pass


# Example Input Tree:
#           3
#          / \
#         5   1
#        / \ / \
#       6  2 0  8
#         / \
#        7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(find_lca(root, 5, 1))
# Example Output: 3
# The LCA of nodes 5 and 1 is 3.

print(find_lca(root, 5, 4))
# Example Output: 5
# The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself.
#
# ------------------------------------------------
