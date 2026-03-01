# ------------------------------------------------
#  *                    Problem 1: Level Order Traversal of Binary Tree
#
#    Given the root of a binary tree, return a list of the level order traversal
#    of its nodes' values (i.e., from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes

    # Add the root to the queue

    # While the queue is not empty:
        # Pop the next node off the queue (pop from the left side!)
        # Add the popped node to the list of explored nodes
        # Add each of the popped node's children to the end of the queue

    # Return the list of visited nodes
    pass


# Example Input Tree:
#      4
#     / \
#    2   6
#   / \
#  1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(level_order(root))

# Example Output: [4, 2, 6, 1, 3]
#
# ------------------------------------------------
