# ------------------------------------------------
#  *                    Problem 5: Find Rightmost Node II
#
#    If you implemented right_most() iteratively in Problem 4, implement it
#    recursively here. If you implemented it recursively, implement it iteratively.
#
#    Evaluate the time complexity of your function.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_most(root):
    # base case
    if root.right.val == None:
        return root.val    
    
    # recursive case
    return right_most(root.right.val)


# Example Input Tree #1:
#        1
#       / \
#      2   5
#     / \
#    4   3
# Input: root = 1 -> Expected Output: 5

# Example Input Tree #2:
#    1
#     \
#      2
#     /
#    3
# Input: root = 1 -> Expected Output: 2
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2

print(right_most(root))
# Input: root = None -> Output: None
#
# ------------------------------------------------
