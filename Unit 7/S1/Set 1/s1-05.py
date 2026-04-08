# ------------------------------------------------
#  *                    Problem 5: Binary Search I
#
#    Binary search is a searching algorithm that allows us to efficiently find the index
#    of a given value within a sorted list. Implement an iterative (non-recursive)
#    implementation of binary search using the pseudocode below.
#
#    Evaluate the time and space complexity of your implementation.
#
#    Pseudocode:
#    - Initialize a left pointer to the 0th index in the list
#    - Initialize a right pointer to the last index in the list
#    - While left pointer is less than right pointer:
#        - Find the middle index of the array
#        - If the value at the middle index is the target value:
#            - Return the middle index
#        - Else if the value at the middle index is less than the target value:
#            - Update pointer(s) to only search right half of the list in next iteration
#        - Else:
#            - Update pointer(s) to only search left half of the list in next iteration
#    - If we search whole list and haven't found target value, return -1


def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))


# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
# Example Output: 5
# Explanation: 11 has index 5 in the list
#
# ------------------------------------------------
