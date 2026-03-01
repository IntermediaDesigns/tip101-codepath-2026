# ------------------------------------------------
#  *                    Problem 1: Level Order Traversal in Dictionary
#
#    Given the root of a binary tree, return a dictionary storing the level
#    order traversal of its nodes' values (from left to right, level by level).
#    Keys are integers representing the level; values are lists of node values.

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_dict(root):
    # If the tree is empty:
    # return an empty dictionary

    # Create an empty dictionary
    # Create an empty queue using deque
    # Append a tuple (root, 1) to the queue (queue stores (node, level) pairs)

    # While the queue is not empty:
        # Pop the next (node, level) pair off the queue (pop from the left side!)
        # If the level is not yet a key in the dictionary, add it with an empty list
        # Append the node's value to dictionary[level]
        # Add each child with incremented level to the end of the queue

    # Return the dictionary
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

print(level_dict(root))

# Example Output: {1: [4], 2: [2, 6], 3: [1, 3]}
#
# ------------------------------------------------
