# ------------------------------------------------
#  *                    Problem 2: 3-Node Sum I
#
#    Given the root of a binary tree that has EXACTLY 3 nodes (root, left child,
#    right child), return True if the value of the root equals the sum of its two
#    children. Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_tree(root):
    if (root.left.val + root.right.val) == root.val:
        return True
    else:
        return False



tree = TreeNode(10, TreeNode(4), TreeNode(6))
print(check_tree(tree))

'''
U: Add the values of the children in a tree with exactly 3 nodes.
    return true if equal to root value, false otherwise

P: Create an if statement to see if the 2 children add to the root value
   if the sum is the same as root, return true
   else, return false

'''
# Example Input Tree #1:
#      10
#     /  \
#    4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2:
#      5
#     / \
#    3   1
# Input: root = 5
# Expected Output: False
#
# ------------------------------------------------
