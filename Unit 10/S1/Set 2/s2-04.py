# ------------------------------------------------
#  *                    Problem 4: Sum Tree
#
#    Given the root of a binary tree, return True if the value of the root
#    equals the sum of the values of all its descendants. Return False otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_root_sum(root):
    pass


# Example Input Tree:
#      14
#     /  \
#    4    6
#   / \
#  3   1

root = TreeNode(14)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)

print(check_root_sum(root))
# Expected Output: True
# 4 + 3 + 1 + 6 = 14

# ------------------------------------------------
