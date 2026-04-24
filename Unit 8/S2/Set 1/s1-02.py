# ------------------------------------------------
#  *                    Problem 2: Binary Tree Height
#
#    Given the root of a binary tree, write a function height() that returns
#    the height of the binary tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def height(root):
    if root is None:
        return 0

    # h = 0

    # if root.left:
    #     h+= height(root.left)
    # else:
    #     h += 1

    # if root.right:
    #     h+= height(root.right)
    # else:
    #     h+= 1

    # return h
    return 1 + max(height(root.left), height(root.right))

tree1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(height(tree1))

# Example Input Tree #1:
#        4
#       / \
#      2   5
#     / \
#    1   3
# Input: root = 4 -> Expected Output: 3

# Example Input Tree #2:
#    4
# Input: root = 4 -> Expected Output: 1
#
# ------------------------------------------------
