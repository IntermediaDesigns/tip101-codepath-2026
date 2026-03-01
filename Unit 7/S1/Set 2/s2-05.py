# ------------------------------------------------
#  *                    Problem 5: Binary Search II
#
#    Given the recursive solution for binary search below, implement an iterative
#    (non-recursive) version of binary search.
#
#    Evaluate the time and space complexity of your implementation.


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_iterative(arr, target):
    pass


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output: 5
# Explanation: 11 has index 5 in the list
#
# ------------------------------------------------
