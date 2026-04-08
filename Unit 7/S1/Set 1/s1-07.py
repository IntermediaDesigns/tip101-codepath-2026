# ------------------------------------------------
#  *                    Problem 7: Find Floor
#
# Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

# Evaluate the time and space complexity of your function.


def find_floor(lst, x):
    left, right = 0, len(lst) - 1
    floor_index = -1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] <= x:
            floor_index = mid
            left = mid + 1
        else:
            right = mid - 1

    return floor_index

print(find_floor([1, 2, 8, 10, 11, 12, 19], 5))


# Example Input: lst = [1, 2, 8, 10, 11, 12, 19], x = 5
# Expected Output: 1
# 2 is the largest element in the list that is less than or equal to 5. 2 has index 1 in the list.
#
# ------------------------------------------------
