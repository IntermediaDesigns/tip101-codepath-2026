# ------------------------------------------------
#  *                    Problem 4: Check Balanced Binary Tree
#
#    Given the root of a binary tree, return True if the tree is balanced,
#    False otherwise. A balanced binary tree is one where the depth of the
#    two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    pass


# Input Tree #1:
#      3
#     / \
#    9  20
#       / \
#      15   7

root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(is_balanced(root1))  # Expected Output: True

# Input Tree #2:
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

print(is_balanced(root2))  # Expected Output: False

# Input Tree #3: Empty Tree
print(is_balanced(None))   # Expected Output: True

# ------------------------------------------------
