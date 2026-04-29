# ------------------------------------------------
#  *                    Problem 4: Find Rightmost Node I
#
#    Given the root of a binary tree, write a function that finds the value of
#    the rightmost node in the tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_most(root):
    current = root

    while current.right:
        current = current.right
    return current.val


# Example Input Tree #1:
#        1
#       / \
#      2   5
#     / \
#    4   3
# Input: root = 1 -> Expected Output: 5

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(5)
node3 = TreeNode(4)
node4 = TreeNode(3)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4

print(right_most(root))

# Example Input Tree #2:
#    1
#     \
#      2
#     /
#    3
# Input: root = 1 -> Expected Output: 2

# Input: root = None -> Output: None
#
# ------------------------------------------------
