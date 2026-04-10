# ------------------------------------------------
#  *                    Problem 2: How Many 1s
#
#    Given a sorted list of integers containing only 0s and 1s, count the total number
#    of 1s in the array in O(log n) time.


def count_ones(lst):
    left, right = 0, len(lst) - 1
    count = 0

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == 1:
            count += (right - mid + 1)
            right = mid - 1
        else:
            left = mid + 1

    return count

print(count_ones([0, 0, 0, 0, 1, 1, 1]))


# Example Input: [0, 0, 0, 0, 1, 1, 1]
# Example Output: 3
#
# ------------------------------------------------
