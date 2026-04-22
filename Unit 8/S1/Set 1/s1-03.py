# ------------------------------------------------
#  *                    Problem 3: 3-Node Sum II
#
#    Given the root of a binary tree that has AT MOST 3 nodes (root, left child,
#    right child), return True if the value of the root equals the sum of the
#    values of its children. Return False otherwise.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_tree(root):
    
    if root == None:
        return False
    sum = 0
    if root.left != None:
        sum += root.left.val
    if root.right != None:
        sum += root.right.val

    if sum == root.val:
        return True
    else:
        return False
    

'''
U: Compare the values of any existing children to root value, return true if equal.
    False otherwise.

P:
'''

tree = TreeNode(10, TreeNode(10))
print(check_tree(tree))


tree2 = TreeNode(10, TreeNode(3), TreeNode(2))
print(check_tree(tree2))

tree3 = TreeNode(10, TreeNode(2))
print(check_tree(tree3))

tree4 = None
print(check_tree(tree4))



# Example Input Tree #1:
#      10
#     /
#    10
# Input: root = 10 -> Expected Output: True

# Example Input Tree #2:
#      5
#     / \
#    3   2
# Input: root = 5 -> Expected Output: True

# Example Input Tree #3:
#      5
#       \
#        2
# Input: root = 5 -> Expected Output: False

# Example Input Tree #4: Empty Tree (None)
# Input: root = None -> Expected Output: False
#
# ------------------------------------------------
