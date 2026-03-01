# ------------------------------------------------
#  *                    Problem 4: Leaf-Similar Trees
#
#    The leaf value sequence of a binary tree is the values of all leaf nodes
#    from left to right. Two binary trees are leaf-similar if their leaf value
#    sequences are the same. Return True if root1 and root2 are leaf-similar,
#    False otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leaf_similar(root1, root2):
    pass


# Input Tree #1:
#         root1                  root2
#           3                      3
#          / \                    / \
#         5   1                  5   1
#        / \ / \                / \ / \
#       6  2 9  8              6  7 4  2
#         / \                          / \
#        7   4                        9   8

r1 = TreeNode(3)
r1.left = TreeNode(5)
r1.right = TreeNode(1)
r1.left.left = TreeNode(6)
r1.left.right = TreeNode(2)
r1.right.left = TreeNode(9)
r1.right.right = TreeNode(8)
r1.left.right.left = TreeNode(7)
r1.left.right.right = TreeNode(4)

r2 = TreeNode(3)
r2.left = TreeNode(5)
r2.right = TreeNode(1)
r2.left.left = TreeNode(6)
r2.left.right = TreeNode(7)
r2.right.left = TreeNode(4)
r2.right.right = TreeNode(2)
r2.right.right.left = TreeNode(9)
r2.right.right.right = TreeNode(8)

print(leaf_similar(r1, r2))  # Expected Output: True
# Both have leaf sequence: [6, 7, 4, 9, 8]

# Input Tree #2:
#   root1     root2
#     1          1
#    / \        / \
#   2   3      3   2

r3 = TreeNode(1, TreeNode(2), TreeNode(3))
r4 = TreeNode(1, TreeNode(3), TreeNode(2))

print(leaf_similar(r3, r4))  # Expected Output: False

# ------------------------------------------------
