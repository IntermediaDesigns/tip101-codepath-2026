# ------------------------------------------------
#  *                    Problem 2: 3-Node Product I
#
#    Given the root of a binary tree that has EXACTLY 3 nodes (root, left child,
#    right child), return True if the value of the root equals the PRODUCT of its
#    two children. Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def check_tree(root):
    if root.left.val * root.right.val == root.val:
        return True
    else:
        return False

root = TreeNode(10)  # Replace with your implementation
node_left = TreeNode(2)
node_right = TreeNode(5)

root.left = node_left
root.right = node_right

print(check_tree(root))
# Example Input Tree #1:
#      10
#     /  \
#    2    5
# Input: root = 10 -> Expected Output: True

# Example Input Tree #2:
#      5
#     / \
#    3   1
# Input: root = 5 -> Expected Output: False
#
# ------------------------------------------------
