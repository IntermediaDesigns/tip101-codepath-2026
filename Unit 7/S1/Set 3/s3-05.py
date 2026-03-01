# ------------------------------------------------
#  *                    Problem 5: Binary Search III
#
#    Implement an iterative (non-recursive) binary search that returns True if the
#    given target is in the list and False otherwise.
#
#    Evaluate the time and space complexity of your implementation.
#
#    Pseudocode:
#    - Initialize a left pointer to the 0th index in the list
#    - Initialize a right pointer to the last index in the list
#    - While left pointer is less than right pointer:
#        - Find the middle index of the array
#        - If the middle value is the target value, return True
#        - If the middle value is smaller than target, search the right half
#        - If the middle value is greater than target, search the left half
#    - Return False if the target element has not been found


def binary_search(lst, target):
    pass


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output: True
#
# ------------------------------------------------
