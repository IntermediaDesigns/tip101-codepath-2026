# ------------------------------------------------
#  *                    Problem 3: 3-Node Product II
#
#    Given the root of a binary tree that has AT MOST 3 nodes (root, left child,
#    right child), return True if the root's value equals the PRODUCT of its
#    children. If the root has only one child, return False.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def check_tree(root):
    if root.left or root.right == None:
        return False
    if root.left.val * root.right.val == root.val:
        return True
    else:
        return False


# Example Input Tree 1
root = TreeNode(5)
node1 = TreeNode(3)
node2 = TreeNode(1)
root.left = node1
root.right = node2

print(check_tree(root))
# Example Input Tree #1:
#      10
#     /
#    10
# Input: root = 10 -> Expected Output: True  (10 * 1? — re-read: only left child -> False per spec)

# Example Input Tree #2:
#      5
#     / \
#    3   1
# Input: root = 5 -> Expected Output: True  (wait: 3*1=3 != 5... check problem — use given examples)

# Example Input Tree #3:
#      5
#       \
#        2
# Input: root = 5 -> Expected Output: False  (only one child)

# Example Input Tree #4: Empty Tree (None)
# Input: root = None -> Expected Output: False
#
# ------------------------------------------------
