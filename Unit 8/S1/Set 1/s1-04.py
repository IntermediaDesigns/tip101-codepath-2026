# ------------------------------------------------
#  *                    Problem 4: Find Leftmost Node I
#
#    Given the root of a binary tree, write a function that finds the value of
#    the leftmost node in the tree.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_most(root):
    if root == None:
        return None

    current = root

    while current.left != None:
        current = current.left
    return current.val

root = TreeNode(1, TreeNode(2), TreeNode(5))
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

print(left_most(root))

root = TreeNode(1, None, TreeNode(2))
root.right.left = TreeNode(3)
print(left_most(root))

rot = None
print(left_most(rot))

'''
U: Return the value of the node most left in a tree

P: while a left node isn't None, move left
    return final node.val
'''

# Example Input Tree #1:
#        1
#       / \
#      2   5
#     / \
#    4   3
# Input: root = 1 -> Expected Output: 4

# Example Input Tree #2:
#    1
#     \
#      2
#     /
#    3
# Input: root = 1 -> Expected Output: 1

# Example Input Tree #3: Empty Tree
# Input: root = None -> Output: None
#
# ------------------------------------------------
