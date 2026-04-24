# ------------------------------------------------
#  *                    Problem 1: Is Uni-valued
#
#    A binary tree is uni-valued if every node in the tree has the same value.
#    Given the root of a binary tree, return True if the tree is uni-valued
#    and False otherwise.
#
#    Evaluate the time complexity of your solution.


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

        def is_univalued(self):
            if self is None:
                return True

            if self.left is not None:
                if self.left.val != self.val:
                    return False
                if self.left.is_univalued() == False:
                    return False

            if self.right is not None:
                if self.right.val != self.val:
                    return False
                if self.right.is_univalued() == False:
                    return False

            return True
    # def is_univalued(root):
    #     if root == None:
    #         return None
    #     if root.val == root:
    #         return True
    #     return is_univalued(root.left)
    #     return is_univalued(root.right)

        def printTree(root):
            if root == None:
                return None
            printTree(root.left)
            print(root.val)
            printTree(root.right)

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)

printTree(root)
is_univalued(root)


# Example Input Tree #1:
#        1
#       / \
#      1   1
#     / \   \
#    1   1   1
# Input: root = 1 -> Expected Output: True

# Example Input Tree #2:
#        1
#       / \
#      1   2
#     / \   \
#    1   1   1
# Input: root = 1 -> Expected Output: False
#
# ------------------------------------------------
