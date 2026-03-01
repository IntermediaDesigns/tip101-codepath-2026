# ------------------------------------------------
#  *                    Problem 5: Merge Sort I
#
#    Merge sort is a sorting algorithm that returns a sorted list in O(n log n) time
#    using a divide and conquer approach. It divides the array into two halves until
#    each sublist has one element, then recursively merges them back in sorted order.
#
#    Given the helper function merge() below, implement merge_sort().


# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(lst):
    pass


# Example Input: [5, 3, 4, 2, 1]
# Example Output: [1, 2, 3, 4, 5]
#
# ------------------------------------------------
