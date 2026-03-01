# ------------------------------------------------
#  *                    Problem 7: Ternary Search
#
#    Ternary search works on a sorted array, similar to binary search, but divides the
#    search interval into THREE parts using two midpoints. This reduces the problem size
#    to approximately one-third in each step.
#
#    Given the pseudocode below, implement ternary_search().
#    Evaluate the time and space complexity of your solution.
#
#    Pseudocode:
#    - Divide the array into three parts using two midpoints (mid1 and mid2).
#    - While the lower bound is <= the upper bound:
#        - If target matches the value at mid1 or mid2 -> return that index
#        - If target < value at mid1 -> search between lower bound and mid1 - 1
#        - If target is between mid1 and mid2 -> search between mid1 + 1 and mid2 - 1
#        - If target > value at mid2 -> search between mid2 + 1 and upper bound
#    - Return -1 if the target is not in the array.


def ternary_search(lst, target):
    pass


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output: 5
# Explanation: 11 has index 5 in the list
#
# ------------------------------------------------
