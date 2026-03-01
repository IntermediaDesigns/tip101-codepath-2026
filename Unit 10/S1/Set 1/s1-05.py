# ------------------------------------------------
#  *                    Problem 5: Sum Root to Leaf Numbers
#
#    Given the root of a binary tree containing digits from 0 to 9 only,
#    each root-to-leaf path represents a number (e.g. 1->2->3 = 123).
#    Return the total sum of all root-to-leaf numbers.
#    A leaf node is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    pass


# Example Input Tree #1:
#      1
#     / \
#    2   3

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

print(sum_numbers(root1))
# Expected Output: 25
# Path 1->2 = 12, Path 1->3 = 13, Sum = 25

# Example Input Tree #2:
#      4
#     / \
#    9   0
#   / \
#  5   1

root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)

print(sum_numbers(root2))
# Expected Output: 1026
# Path 4->9->5 = 495, Path 4->9->1 = 491, Path 4->0 = 40, Sum = 1026

# ------------------------------------------------
