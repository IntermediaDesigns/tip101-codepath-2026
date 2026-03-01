# ------------------------------------------------
#  *                    Problem 5: Merge Sort II
#
#    Merge sort is a sorting algorithm that returns a sorted list in O(n log n) time
#    using a divide and conquer approach.
#
#    Given the main function merge_sort() below, implement the helper function merge().
#    merge() accepts two sorted lists (left and right) and returns a single sorted list.


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


def merge(left, right):
    pass


# Example Input: left = [1, 3, 5], right = [2, 4]
# Example Output: [1, 2, 3, 4, 5]
#
# ------------------------------------------------
